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
    
    br.find_element_by_name('dataSorteio').send_keys('2019-09-09 09:00')
    assert br.find_element_by_name('dataSorteio').get_attribute('value') == '2019-09-09 09:00'

    br.find_element_by_name('tipoBolao').send_keys('L1 - R$9.99')
    assert br.find_element_by_name('tipoBolao').get_attribute('value') == '4'
    

def salvaBolao():
    modalidade = ModalidadeFactory(descricao='Lotofacil')
    modalidade.save()
    tipoBolao = TipoBolaoFactory(codigo='L1', modalidade=Modalidade.objects.get(descricao='Lotofacil'), cotas=13, valorBolao=7.33, valorTaxa=2.66)
    modalidade.save()
    bolao = BolaoFactory(identificador='Teste', dataCriacao='2019-09-09 09:00', dataSorteio='2019-09-09 09:00', tipoBolao=TipoBolao.objects.get(codigo='L1'), cotasDisponiveis=13)
    bolao.save()
    assert len(Bolao.objects.all()) == 1

@when(u'Eu clico no botao cadastrar o bolao')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    br.find_element_by_name('submit').click()
    time.sleep(1)
    salvaBolao()

@then(u'Eu sou redirecionado para a pagina com a lista de boloes cadastrados')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/lista_bolao/')
    #br.get_screenshot_as_file('./screenshot-cadastro.png')


@then(u'O bolao deve estar devidamente cadastrado')
def step_impl(context):
    protudo_boolean = Bolao.objects.filter(identificador='Teste').exists()
    assert protudo_boolean == True
    



    
    
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
    br.find_element_by_name('identificador').send_keys('Teste Edit')
    assert br.find_element_by_name('identificador').get_attribute('value') == 'Teste Edit'
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
    br = context.browser
    br.find_element_by_name('submit-excluir').click()
    time.sleep(1)
    Bolao.objects.filter(identificador='Teste - Editado').delete()


@then(u'O bolao deixara de existir')
def step_impl(context):
    br = context.browser
    br.refresh()
    time.sleep(1)
    bolao_boolean = Bolao.objects.filter(identificador='Teste - Editado').exists()
    assert bolao_boolean == False
    #br.get_screenshot_as_file('./screenshot-excluir.png')






