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

def carregaBaseGuiches():
    guiche1 = GuicheFactory(numero=1, descricao='Idosos', codigoCEF=190901)
    guiche1.save()
    guiche2 = GuicheFactory(numero=2, descricao='Somente Jogos', codigoCEF=190902)
    guiche2.save()
    guiche3 = GuicheFactory(numero=3, descricao='Normal', codigoCEF=190903)
    guiche3.save()
    assert len(Guiche.objects.all()) == 3

@given(u'Eu estou na pagina de cadastrado de guiche')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/cadastro_guiche')
    carregaBaseGuiches()
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/cadastro_guiche/')
    #carregaGuichesCadastrados()
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot1.png')
    
    

@given(u'Eu informo um numero do guiche ainda nao cadastrado')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    guiche_boolean = Guiche.objects.filter(numero=9).exists()
    assert guiche_boolean == False
    
    br.find_element_by_name('numero').send_keys(9)
    assert br.find_element_by_name('numero').get_attribute('value') == '9'

    time.sleep(1)
    br.get_screenshot_as_file('./screenshot2.png')


@given(u'Eu informo a descricao do guiche')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('descricao').send_keys('Teste')
    assert br.find_element_by_name('descricao').get_attribute('value') == 'Teste'
    
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot3.png')
    

@given(u'Eu informo um codigoCEF do guiche ainda nao cadastrado')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    guiche_boolean = Guiche.objects.filter(codigoCEF=999999).exists()
    assert guiche_boolean == False
    
    br.find_element_by_name('codigoCEF').send_keys(999999)
    assert br.find_element_by_name('codigoCEF').get_attribute('value') == '999999'

    time.sleep(1)
    br.get_screenshot_as_file('./screenshot4.png')


def salvaGuiche():
    guiche = GuicheFactory(numero=9, descricao='Normal Teste', codigoCEF=999999)
    guiche.save()
    assert len(Guiche.objects.all()) == 4

@when(u'Eu clico no botao cadastrar o guiche')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('submit').click()
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot5.png')
    salvaGuiche()


@then(u'Eu sou redirecionado para a pagina com a lista de guiches cadastrados')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/lista_guiche/')


@then(u'O guiche deve estar devidamente cadastrado')
def step_impl(context):
    br = context.browser

    guiche_boolean = Guiche.objects.filter(numero=9).exists()
    assert guiche_boolean == True
    

### TESTE: Guiche editado com sucesso



### TESTE: Guiche excluido com sucesso 



