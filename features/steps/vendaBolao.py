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


def criarNovoUsuario():
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='admin', email='admin@example.com')
    u.set_password('admin12345')
    # Don't omit to call save() to insert object in database
    u.save()

#Scenario: Campos Vazios
@given('Eu sou um usuario logado')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/logout/')
    time.sleep(1)
    
    #Cria um usuário de teste
    criarNovoUsuario()
    
    br.get('https://geelo.herokuapp.com/')
    
    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('admin')
    br.find_element_by_name('password').send_keys('admin12345')
    br.find_element_by_name('action-login').click()


    
    
### TEST: Verificar cadastros    
@given(u'Eu possuo tipo de funcionario cadastrado no sistema')
def step_impl(context):
    descricao = TipoFuncionarioFactory(descricao='Vendedor')

    descricao.save()
    assert len(TipoFuncionario.objects.all()) == 1

    
@given(u'Eu possuo funcionario cadastrado no sistema')
def step_impl(context):
    user_root = User.objects.get(username='admin')
    tipo_funcionario = TipoFuncionario.objects.get(descricao='Vendedor')
    
    funcionario = FuncionarioFactory(user=user_root, tipoFuncionario=tipo_funcionario, nome='Thales', sobrenome='C. Vescovi', cpf='147.231.177-22', rg='3.206.960', ctps='999-9' , dataContratacao='2017-08-12 12:00:00' , dataDemissao='2017-08-12 12:00:00' , salario=150.00)
    funcionario.save()
    assert len(Funcionario.objects.all()) == 1


@given(u'Eu possuo guiche cadastrado no sistema')
def step_impl(context):
    guiche = GuicheFactory(numero=1, descricao='Prioritario Jogos', codigoCEF=191902)
    guiche.save()
    assert len(Guiche.objects.all()) == 1


@given(u'Eu possuo modalidade cadastrado no sistema')
def step_impl(context):
    modalidade = ModalidadeFactory(descricao='Telesena')
    modalidade.save()
    modalidade2 = ModalidadeFactory(descricao='Mega-Sena')
    modalidade2.save()
    assert len(Modalidade.objects.all()) == 2


@given(u'Eu possuo produto cadastrado no sistema')
def step_impl(context):
    produto = ProdutoFactory(descricao='Telesena de Fim de ano', valorProduto=10.01, valorComissao=0.45, modalidade=Modalidade.objects.get(descricao='Telesena'), quantidadeDisponivel=150, dataSorteio='2018-01-01 19:00')
    produto.save()
    assert len(Produto.objects.all()) == 1


@given(u'Eu possuo tipo de bolao cadastrado no sistema')
def step_impl(context):
    tipo_bolao = TipoBolaoFactory(codigo='T1', modalidade=Modalidade.objects.get(descricao='Mega-Sena'), cotas=8, valorBolao=7.30 , valorTaxa=3.40)
    tipo_bolao.save()
    assert len(TipoBolao.objects.all()) == 1


@given(u'Eu possuo bolao cadastrado no sistema')
def step_impl(context):
    bolao = BolaoFactory(identificador='T', dataCriacao='2018-01-01 10:00', dataSorteio='2018-01-01 19:00', tipoBolao=TipoBolao.objects.get(codigo='T1'), cotasDisponiveis='8')
    bolao.save()
    assert len(Bolao.objects.all()) == 1
    




### TEST: Efetuar Venda de Bolão
def carregaBoloes():
    boloes = Bolao.objects.all()
    boloes_validos = boloes.filter(cotasDisponiveis__gte=1,dataSorteio__gte=datetime.now())
    assert len(Bolao.objects.all()) > 0


@given(u'Eu estou na pagina de vendas de bolao')
def step_impl(context):
    carregaBoloes()
    
    br = context.browser
    br.get('https://geelo.herokuapp.com/realiza_venda_bolao')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/realiza_venda_bolao/')
    #br.get_screenshot_as_file('./screenshot1.png')
    

@when(u'Eu clico no botao vender bolao')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('vender-bolao').click()
    time.sleep(1)
    #br.get_screenshot_as_file('./screenshot2.png')


@then(u'Eu confirmo a venda do bolao')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('confirmar-venda').click()
    time.sleep(2)
    #br.get_screenshot_as_file('./screenshot3.png')
    

@then(u'A venda do bolao e efetuada e eu volto para a tela de vendas')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/realiza_venda_bolao')
    
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/realiza_venda_bolao/')
    #br.get_screenshot_as_file('./screenshot4.png')
    
    
    
### TEST: Cancelar Venda de Bolão

@given(u'Eu estou na pagina de vendas do bolao')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/realiza_venda_bolao')
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/realiza_venda_bolao/')
    

@then(u'Eu cancelo a venda do bolao')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('cancelar_venda').click()
    time.sleep(1)
    

@then(u'A venda do bolao nao e efetuada e eu volto para a tela de vendas')
def step_impl(context):
    br = context.browser
    #Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/realiza_venda_bolao/')