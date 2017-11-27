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


### TEST: Verificar cadastros ###


### TEST: Efetuar Venda de Produto
def carregaProdutos():
    produtos = Produto.objects.all()
    produtos_validos = produtos.filter(dataSorteio__gte=datetime.now())
    assert len(Produto.objects.all()) > 0

@given(u'Eu estou na pagina de vendas de produto')
def step_impl(context):
    carregaProdutos()
    
    br = context.browser
    br.get('https://geelo.herokuapp.com/realiza_venda_produto')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/realiza_venda_produto/')
    #br.get_screenshot_as_file('./screenshot1.png')
    

@when(u'Eu clico no botao vender produto')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('vender-produto').click()
    time.sleep(1)
    #br.get_screenshot_as_file('./screenshot2.png')


@then(u'Eu confirmo a venda do produto')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('confirmar-venda').click()
    time.sleep(2)
    #br.get_screenshot_as_file('./screenshot3.png')
    

@then(u'A venda do produto e efetuada e eu volto para a tela de vendas')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/realiza_venda_produto')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/realiza_venda_produto/')
    #br.get_screenshot_as_file('./screenshot4.png')
    
    
    
### TEST: Cancelar Venda de Bolão

@given(u'Eu estou na pagina de vendas do produto')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/realiza_venda_produto')
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/realiza_venda_produto/')
    

@then(u'Eu cancelo a venda do produto')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('cancelar-venda').click()
    time.sleep(1)


@then(u'A venda do produto nao e efetuada e eu volto para a tela de vendas')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/realiza_venda_produto/')