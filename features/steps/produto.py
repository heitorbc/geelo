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


@given(u'Eu informo a descricao, valor do produto, valor da comissao, modalidade, quantidade disponivel e data/hora')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    br.find_element_by_name('descricao').send_keys('Teste')
    assert br.find_element_by_name('descricao').get_attribute('value') == 'Teste'
    br.get_screenshot_as_file('./screenshot2.png')
    
    br.find_element_by_name('valorProduto').send_keys(9)
    assert br.find_element_by_name('valorProduto').get_attribute('value') == '9'
    br.get_screenshot_as_file('./screenshot3.png')
    
    br.find_element_by_name('valorComissao').send_keys(1)
    assert br.find_element_by_name('valorComissao').get_attribute('value') == '1'
    br.get_screenshot_as_file('./screenshot4.png')
    
    br.find_element_by_name('modalidade').send_keys('Telesena')
    assert br.find_element_by_name('modalidade').get_attribute('value') == '4'
    br.get_screenshot_as_file('./screenshot5.png')
    
    br.find_element_by_name('quantidadeDisponivel').send_keys(9)
    assert br.find_element_by_name('quantidadeDisponivel').get_attribute('value') == '9'
    br.get_screenshot_as_file('./screenshot6.png')

    br.find_element_by_name('dataSorteio').send_keys('2019-09-09 19:00')
    assert br.find_element_by_name('dataSorteio').get_attribute('value') == '2019-09-09 19:00'
    br.get_screenshot_as_file('./screenshot7.png')


def salvaProduto():
    modalidade = ModalidadeFactory(descricao='Telesena')
    modalidade.save()
    produto = ProdutoFactory(descricao='Teste', valorProduto=9.00, valorComissao=1.00, modalidade=Modalidade.objects.get(descricao='Telesena'), quantidadeDisponivel=9, dataSorteio='2019-09-09 19:00')
    produto.save()
    assert len(Produto.objects.all()) == 1

@when(u'Eu clico no botao cadastrar o produto')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('submit').click()
    time.sleep(1)
    salvaProduto()


@then(u'Eu sou redirecionado para a pagina com a lista de produtos cadastrados')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/lista_produto/')


@then(u'O produto deve estar devidamente cadastrado')
def step_impl(context):
    protudo_boolean = Produto.objects.filter(descricao='Teste').exists()
    assert protudo_boolean == True



    
    
### TESTE: Guiche editado com sucesso
@given(u'Estou na pagina de lista de produtos')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/lista_produto')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/lista_produto/')
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot1.png')


@given(u'Seleciono o botao editar de um produto')
def step_impl(context):
    br = context.browser
    indice = br.find_element_by_xpath("//td[@id='id']")

    print("ID: " + str(indice))
    
    #br.get('https://geelo.herokuapp.com/produto/%d/editar/' % produto[0].id)
    
    br.find_element_by_name('submit-vizualizar').click()
    time.sleep(1)
    br.get_screenshot_as_file('./screenshot2.png')


@given(u'Sou redirecionado para a pagina com os dados do produto ja preenchidos')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/editar')


@given(u'Preencho o campo valor da comissao com um novo valor')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Preencho o campo valor da comissao com um novo valor')


@when(u'Clico no botao editar o produto')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Clico no botao editar o produto')





### TESTE: Guiche excluido com sucesso 
@when(u'Clico no botao excluir o produto')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Clico no botao excluir o produto')

@then(u'O produto deixara de existir')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then O produto deixara de existir')


