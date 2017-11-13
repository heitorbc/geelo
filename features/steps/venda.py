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


def criarNovoUsuario():
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='admin', email='admin@example.com')
    u.set_password('admin123456')
    # Don't omit to call save() to insert object in database
    u.save()

#Scenario: Campos Vazios
@given('Eu sou um usuario logado')
def step_impl(context):
    #Cria um usuário de teste
    criarNovoUsuario()
    
    br = context.browser
    br.get('https://geelo.herokuapp.com/')
    
    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('admin')
    br.find_element_by_name('password').send_keys('admin123456')
    br.find_element_by_name('action-login').click()

    

@given(u'Eu estou na pagina principal')
def step_impl(context):
    br = context.browser
    #br.get_screenshot_as_file('./screenshot.png')
    
    # Checks for Cross-Site Request Forgery protection input
    assert br.current_url.endswith('/home/')
    
    
    
# TEST: Verificar cadastros    
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
    



# TEST: Abrir tela de vendas e carregar bolões disponíveis
@when(u'Eu clico na aba vender')
def step_impl(context):
    #br = context.browser
    #br.get('https://geelo.herokuapp.com/')
    #assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    #br.find_element_by_name('submit_venda_bolao').click()
    pass
    

@then(u'Sou redirecionado para a pagina de vendas')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/realiza_venda_bolao')
    #assert br.current_url.endswith('/realiza_venda/')
    br.get_screenshot_as_file('./screenshot.png')


@then(u'Carrego os boloes disponiveis na tela')
def step_impl(context):
    boloes = Bolao.objects.all()
    boloes_validos = boloes.filter(cotasDisponiveis__gte=1,dataSorteio__gte=datetime.now())
    assert len(TipoBolao.objects.all()) > 0




# TEST: Efetuar Venda de Bolão
@given(u'Eu estou na pagina de vendas')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/realiza_venda')

    # Checks for Cross-Site Request Forgery protection input
    #assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    #assert br.current_url.endswith('/realiza_venda/')


@when(u'Eu clico no botao vender')
def step_impl(context):
    br = context.browser
    #assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    br.find_element_by_name('Vender').click()


@then(u'A venda e efetuada e armazenada')
def step_impl(context):
    bolao = get_object_or_404(Bolao, pk=pk)
    bolao.vende_cota()
    Venda.objects.create(vendedor=request.user, bolao=bolao, dataHoraVenda=datetime.now(), guiche=Guiche.objects.get(numero='1'))
    bolao.save()
    return redirect('/realiza_venda')


    
    
    




