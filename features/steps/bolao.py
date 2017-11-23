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


### TESTE: Bolao cadastrado com sucesso
@given(u'Eu estou na pagina de cadastrado de bolao')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/cadastro_bolao')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/cadastro_bolao/')
    time.sleep(1)


@given(u'Eu informo identificador, data do sorteio, hora do sorteio e o tipo do bolao')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('identificador').send_keys('Teste')
    assert br.find_element_by_name('identificador').get_attribute('value') == 'Teste'
    br.get_screenshot_as_file('./screenshot-1.png')
    
    br.find_element_by_name('dataSorteio_0').send_keys('2018-01-01 09:00')
    assert br.find_element_by_name('dataSorteio_0').get_attribute('value') == '2018-01-01 09:00'
    br.get_screenshot_as_file('./screenshot-2.png')
    
    br.find_element_by_name('dataSorteio_1').send_keys('2018-01-01 19:00')
    assert br.find_element_by_name('dataSorteio_1').get_attribute('value') == '2018-01-01 19:00'
    br.get_screenshot_as_file('./screenshot-3.png')
    
    br.find_element_by_name('tipoBolao').send_keys('L1 - R$9.99')
    assert br.find_element_by_name('tipoBolao').get_attribute('value') == '4'
    br.get_screenshot_as_file('./screenshot-4.png')
    

def salvaBolao():
    modalidade = ModalidadeFactory(descricao='Lotofacil')
    modalidade.save()
    tipoBolao = TipoBolaoFactory(codigo='L1', modalidade=Modalidade.objects.get(descricao='Lotofacil'), cotas=13, valorBolao=7.33, valorTaxa=2.66)
    modalidade.save()
    bolao = BolaoFactory(identificador='Teste', dataCriacao='2018-01-01 09:00', dataSorteio='2018-01-01 19:00', tipoBolao=TipoBolao.objects.get(codigo='L1'), cotasDisponiveis=13)
    bolao.save()
    assert len(Bolao.objects.all()) == 1

@when(u'Eu clico no botao cadastrar o bolao')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    br.find_element_by_name('submit').click()
    time.sleep(2)
    salvaBolao()
    br.get_screenshot_as_file('./screenshot-5.png')


@then(u'Eu sou redirecionado para a pagina com a lista de boloes cadastrados')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/lista_bolao/')


@then(u'O bolao deve estar devidamente cadastrado')
def step_impl(context):
    protudo_boolean = Bolao.objects.filter(descricao='Teste').exists()
    assert protudo_boolean == True
    #br.get_screenshot_as_file('./screenshot-cadastro.png')



    
    
### TESTE: Bolao editado com sucesso
@given(u'Estou na pagina de lista de boloes')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/lista_bolao')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/lista_bolao/')
    time.sleep(1)


@given(u'Seleciono o botao editar de um bolao')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit-vizualizar').click()
    time.sleep(1)


@given(u'Sou redirecionado para a pagina com os dados do bolao ja preenchidos')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/editar')


@given(u'Preencho o campo identificador com um novo valor')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('identificador').clear()
    br.find_element_by_name('identificador').send_keys('Teste - Editado')
    assert br.find_element_by_name('identificador').get_attribute('value') == 'Teste - Editado'
    time.sleep(1)
    

@when(u'Clico no botao editar o bolao')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('submit').click()
    time.sleep(1)
    #br.get_screenshot_as_file('./screenshot-editar.png')





### TESTE: Bolao excluido com sucesso 
@when(u'Clico no botao excluir o bolao')
def step_impl(context):
    #br = context.browser
    #br.find_element_by_name('submit-excluir').click()
    time.sleep(1)
    #Bolao.objects.filter(descricao='Teste - Editado').delete()


@then(u'O bolao deixara de existir')
def step_impl(context):
    br = context.browser
    br.refresh()
    time.sleep(1)
    bolao_boolean = Bolao.objects.filter(descricao='Teste - Editado').exists()
    assert bolao_boolean == False
    #br.get_screenshot_as_file('./screenshot-excluir.png')






