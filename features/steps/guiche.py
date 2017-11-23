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
    guiche1 = GuicheFactory(numero=1, descricao='Prioritario Jogos', codigoCEF=191901)
    guiche1.save()
    guiche2 = GuicheFactory(numero=2, descricao='Normal', codigoCEF=191902)
    guiche2.save()
    guiche3 = GuicheFactory(numero=3, descricao='Prioritario Idoso', codigoCEF=191903)
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
    time.sleep(1)

    
@given(u'Eu informo um numero do guiche ainda nao cadastrado')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    guiche_boolean = Guiche.objects.filter(numero=99).exists()
    assert guiche_boolean == False
    
    br.find_element_by_name('numero').send_keys(99)
    assert br.find_element_by_name('numero').get_attribute('value') == '99'
    time.sleep(1)



@given(u'Eu informo a descricao do guiche')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('descricao').send_keys('Teste')
    assert br.find_element_by_name('descricao').get_attribute('value') == 'Teste'
    time.sleep(1)

    

@given(u'Eu informo um codigoCEF do guiche ainda nao cadastrado')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    guiche_boolean = Guiche.objects.filter(codigoCEF=191999).exists()
    assert guiche_boolean == False
    
    br.find_element_by_name('codigoCEF').send_keys(191999)
    assert br.find_element_by_name('codigoCEF').get_attribute('value') == '191999'
    time.sleep(1)


def salvaGuiche():
    guiche = GuicheFactory(numero=99, descricao='Teste', codigoCEF=191999)
    guiche.save()
    assert len(Guiche.objects.all()) == 4

@when(u'Eu clico no botao cadastrar o guiche')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('submit').click()
    time.sleep(1)
    salvaGuiche()


@then(u'Eu sou redirecionado para a pagina com a lista de guiches cadastrados')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/lista_guiche/')


@then(u'O guiche deve estar devidamente cadastrado')
def step_impl(context):
    guiche_boolean = Guiche.objects.filter(numero=99).exists()
    assert guiche_boolean == True
    #br.get_screenshot_as_file('./screenshot-cadastro.png')
    




### TESTE: Guiche editado com sucesso
@given(u'Estou na pagina de lista de guiches')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/lista_guiche')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/lista_guiche/')
    time.sleep(1)


@given(u'Seleciono o botao editar de um guiche')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit-vizualizar').click()
    time.sleep(1)


@given(u'Sou redirecionado para a pagina com os dados do guiche ja preenchidos')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/editar')


@given(u'Preencho o campo descricao com um novo nome')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('descricao').clear()
    br.find_element_by_name('descricao').send_keys('Teste - Editado')
    assert br.find_element_by_name('descricao').get_attribute('value') == 'Teste - Editado'
    time.sleep(1)


@when(u'Clico no botao editar o guiche')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('submit').click()
    time.sleep(1)
    #br.get_screenshot_as_file('./screenshot-editar.png')



### TESTE: Guiche excluido com sucesso 
@when(u'Clico no botao excluir o guiche')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit-excluir').click()
    time.sleep(1)
    Guiche.objects.filter(numero=99).delete()
    
@then(u'O guiche deixara de existir')
def step_impl(context):
    br = context.browser
    br.refresh()
    time.sleep(1)
    guiche_boolean = Guiche.objects.filter(numero=99).exists()
    assert guiche_boolean == False
    #br.get_screenshot_as_file('./screenshot-excluir.png')