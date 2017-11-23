from behave import *
from app.models import *
from app.views import *
from django.contrib.auth.models import User
from test.factories.user import UserFactory
from test.factories.tipo_funcionario import TipoFuncionarioFactory
from test.factories.funcionario import FuncionarioFactory
from test.factories.bolao import BolaoFactory
from test.factories.guiche import GuicheFactory
from test.factories.produto import ProdutoFactory
from test.factories.modalidade import ModalidadeFactory
from test.factories.tipo_bolao import TipoBolaoFactory
import time



### USUARIO LOGADO ###



### TESTE: Funcionario cadastrado com sucesso
@given(u'Eu estou na pagina de cadastrado de funcionario')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/cadastro_funcionario')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/cadastro_funcionario/')
    time.sleep(1)


@given(u'Eu informo o primeiro e segundo nome, usuario, email e password')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('first_name').send_keys('Teste')
    assert br.find_element_by_name('first_name').get_attribute('value') == 'Teste'
    
    br.find_element_by_name('last_name').send_keys('T. Testado')
    assert br.find_element_by_name('last_name').get_attribute('value') == 'T. Testado'

    user_root_boolean = User.objects.filter(username='teste').exists()
    assert user_root_boolean == False
    br.find_element_by_name('username').send_keys('teste')
    assert br.find_element_by_name('username').get_attribute('value') == 'teste'
    
    br.find_element_by_name('email').send_keys('teste@teste.com')
    assert br.find_element_by_name('email').get_attribute('value') == 'teste@teste.com'
    
    br.find_element_by_name('password').send_keys('teste123456')
    assert br.find_element_by_name('password').get_attribute('value') == 'teste123456'
    

@when(u'Eu clico no botao cadastrar o funcionario')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    br.find_element_by_name('submit').click()
    time.sleep(1)
    #br.get_screenshot_as_file('./screenshot-cadastro1.png')
    

@then(u'Eu sou redirecionado para a pagina com a lista de funcionarios cadastrados')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/lista_funcionario/')



@given(u'Estou na pagina de lista de funcionarios')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/lista_funcionario')
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/lista_funcionario/')
    time.sleep(1)


@given(u'Eu clico no botao vizualizar dados para finalizar o cadastro')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit-vizualizar-user').click()
    time.sleep(1)


@given(u'Eu informo o tipo do funcionario, cpf, rg, ctps e salario')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('tipoFuncionario').send_keys('Vendedor')
    assert br.find_element_by_name('tipoFuncionario').get_attribute('value') == '1'
    
    funcionario_cpf_boolean = Funcionario.objects.filter(cpf='000.000.000-91').exists()
    assert funcionario_cpf_boolean == False
    br.find_element_by_name('cpf').send_keys('000.000.000-91')
    assert br.find_element_by_name('cpf').get_attribute('value') == '000.000.000-91'

    funcionario_rg_boolean = Funcionario.objects.filter(rg='1.234.567').exists()
    assert funcionario_rg_boolean == False
    br.find_element_by_name('rg').send_keys('1.234.567')
    assert br.find_element_by_name('rg').get_attribute('value') == '1.234.567'

    br.find_element_by_name('ctps').send_keys('99999')
    assert br.find_element_by_name('ctps').get_attribute('value') == '99999'

    br.find_element_by_name('salario').clear()
    br.find_element_by_name('salario').send_keys(1500)
    assert br.find_element_by_name('salario').get_attribute('value') == '1500'


def criarNovoUser():
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='admin', email='admin@example.com')
    u.set_password('admin123456')
    # Don't omit to call save() to insert object in database
    u.save()
    
def criarTipoFuncionario():
    t = TipoFuncionarioFactory(descricao='Vendedor')
    # Don't omit to call save() to insert object in database
    t.save()

def salvaFuncionario():
    criarNovoUser()
    user_root = User.objects.get(username='admin')
    criarTipoFuncionario()
    tipo_funcionario = TipoFuncionario.objects.get(descricao='Vendedor')
    funcionario = FuncionarioFactory(user=user_root, tipoFuncionario=tipo_funcionario, nome='Teste', sobrenome='T. Testado', cpf='000.000.000-91', rg='1.234.567', ctps='99999' , dataContratacao='2017-11-22 12:00:00' , dataDemissao='2017-11-22 12:00:00' , salario=1500.00)
    funcionario.save()
    assert len(Funcionario.objects.all()) == 1

@when(u'Eu clico no botao editar dados do funcionario')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    br.find_element_by_name('submit').click()
    time.sleep(1)
    salvaFuncionario()
    #br.get_screenshot_as_file('./screenshot-cadastro2.png')
    
    
@then(u'O funcionario deve estar devidamente cadastrado')
def step_impl(context):
    funcionario_boolean = Funcionario.objects.filter(cpf='000.000.000-91').exists()
    assert funcionario_boolean == True
    
    
   
   
### TESTE: Funcionario editado com sucesso
@given(u'Seleciono o botao vizualizar acesso de um funcionario')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit-vizualizar').click()
    time.sleep(1)


@given(u'Sou redirecionado para a pagina com os dados do funcionario ja preenchidos')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/editar')


@given(u'Preencho o campo primeiro nome com um novo valor')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('first_name').clear()
    br.find_element_by_name('first_name').send_keys('Teste - Editado')
    assert br.find_element_by_name('first_name').get_attribute('value') == 'Teste - Editado'

    # autenticação para edição
    br.find_element_by_name('password').clear()
    br.find_element_by_name('password').send_keys('teste123456')
    assert br.find_element_by_name('password').get_attribute('value') == 'teste123456'
    time.sleep(1)
    

@when(u'Clico no botao editar o funcionario')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('submit').click()
    time.sleep(1)
    #br.get_screenshot_as_file('./screenshot-editar.png')
    
    
### TESTE: Funcionario excluido com sucesso 
@when(u'Clico no botao excluir o funcionario')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit-excluir').click()
    time.sleep(1)
    Funcionario.objects.filter(cpf='000.000.000-91').delete()


@then(u'O funcionario deixara de existir')
def step_impl(context):
    br = context.browser
    br.refresh()
    time.sleep(1)
    funcionario_boolean = Funcionario.objects.filter(cpf='000.000.000-91').exists()
    assert funcionario_boolean == False
    #br.get_screenshot_as_file('./screenshot-excluir.png')
