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


### TESTE: Produto cadastrado com sucesso
@given(u'Eu estou na pagina de cadastrado de produto')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/cadastro_produto')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/cadastro_produto/')
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot1.png')


@given(u'Eu informo a descricao do produto')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('descricao').send_keys('Telesena de Teste')
    assert br.find_element_by_name('descricao').get_attribute('value') == 'Telesena de Teste'
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot2.png')


@given(u'Eu informo o valor do produto')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('valorProduto').send_keys(9.99)
    assert br.find_element_by_name('valorProduto').get_attribute('value') == '9.99'
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot3.png')


@given(u'Eu informo o valor da comissao')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('valorComissao').send_keys(0.99)
    assert br.find_element_by_name('valorComissao').get_attribute('value') == '0.99'
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot4.png')



@given(u'Eu informo a modalidade do produto')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('modalidade').send_keys(Modalidade.objects.get(descricao='Telesena'))
    assert br.find_element_by_name('modalidade').get_attribute('value') == 'Telesena'
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot5.png')


@given(u'Eu informo a quantidade disponivel do produto')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('quantidadeDisponivel').send_keys(99)
    assert br.find_element_by_name('quantidadeDisponivel').get_attribute('value') == '99'
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot6.png')


@given(u'Eu informo a data/hora do sorteio')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('dataSorteio').send_keys('2019-09-09 19:00')
    assert br.find_element_by_name('dataSorteio').get_attribute('value') == '2019-09-09 19:00'
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot7.png')


@when(u'Eu clico no botao cadastrar o produto')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Eu informo a data/hora do sorteio')


@then(u'Eu sou redirecionado para a pagina com a lista de produtos cadastrados')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Eu sou redirecionado para a pagina com a lista de produtos cadastrados')


@then(u'O produto deve estar devidamente cadastrado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then O produto deve estar devidamente cadastrado')