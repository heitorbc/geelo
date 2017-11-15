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



### TESTE: Guiche cadastrado com sucesso
@given(u'Estou na pagina de cadastrado de guiche')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/cadastro_guiche')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/cadastro_guiche/')
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot1.png')
    
    
    

@given(u'Informo um numero do guiche ainda nao cadastrado')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    numero = Guiche.objects.filter(numero=9).exists()
    assert numero == False
    
    br.find_element_by_name('numero').send_keys(9)
    assert br.find_element_by_name('numero').get_attribute('value') == '9'

    time.sleep(1)
    br.get_screenshot_as_file('./screenshot2.png')


@given(u'Informo a descricao do guiche')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('descricao').send_keys('Normal')
    assert br.find_element_by_name('descricao').get_attribute('value') == 'Normal'
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot3.png')
    

@given(u'Informo um codigoCEF do guiche ainda nao cadastrado')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    codigoCEF = Guiche.objects.filter(codigoCEF=999999).exists()
    assert codigoCEF == False
    
    br.find_element_by_name('codigoCEF').send_keys(999999)
    assert br.find_element_by_name('codigoCEF').get_attribute('value') == '999999'

    time.sleep(1)
    br.get_screenshot_as_file('./screenshot4.png')


@when(u'Clico no botao cadastrar')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('submit').click()
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot5.png')


@then(u'Sou redirecionado para a pagina com a lista de guiches cadastrados')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/lista_guiche/')


@then(u'O guiche deve estar devidamento cadastrado')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/lista_guiche/')

    guiche = Guiche.objects.all()
    ultimo_guiche = guiche.filter(numero=9)
    
    Guiche.__str__()
    
    
    #assert ultimo_guiche.numero == 9
    
    #print(br.find_element_by_id('numero').get_attribute(guiche))
    #print(br.find_element_by_id('numero').get_attribute(guiche[len(guiches)]))
    
    
    #assert br.find_element_by_id('numero').get_attribute(guiche[len(guiches)]) == '9'
    
    
### TESTE: Guiche editado com sucesso    

### TESTE: Guiche excluido com sucesso 