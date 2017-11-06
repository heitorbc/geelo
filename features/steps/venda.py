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


    
@given(u'Eu possuo usuarios cadastrados no sistema')
def step_impl(context):
    user_heitor = UserFactory(username='heitor', email='heitorhbc@gmail.com', password='admin123456')
    user_thales = UserFactory(username='thales', email='thalescarreta@gmail.com', password='admin123456')
    user_root = UserFactory(username='admin', email='superuser@gmail.com', password='admin123456')
    
    lista_usuarios = [user_heitor, user_thales, user_root]
    
    salva_participantes(lista_usuarios)
    assert len(User.objects.all()) == 3



@given(u'Eu possuo tipo de funcionario cadastrado no sistema')
def step_impl(context):
    descricao = TipoFuncionarioFactory(descricao='Vendedor')

    descricao.save()
    assert len(TipoFuncionario.objects.all()) == 1

    
    
@given(u'Eu possuo funcionario cadastrado no sistema')
def step_impl(context):
    user_root = User.objects.get(username='thales')
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
    tipoBolao = TipoBolaoFactory(codigo='M1', modalidade=Modalidade.objects.get(descricao='Mega-Sena'), cotas=8, valorBolao=7.30 , valorTaxa=3.40)
    tipoBolao.save()
    assert len(TipoBolao.objects.all()) == 1

@given(u'Eu possuo bolao cadastrado no sistema')
def step_impl(context):
    bolao = BolaoFactory(identificador='A', dataCriacao='2018-01-01 10:00', dataSorteio='2018-01-01 19:00', tipoBolao=TipoBolao.objects.get(codigo='M1'), cotasDisponiveis='8')
    bolao.save()
    assert len(Bolao.objects.all()) == 1

@when(u'Eu chamo a funcao efetuar venda')
def step_impl(context):
    pass

@then(u'A venda é efetuada')
def step_impl(context):
    pass

@then(u'A venda é armazenada no sistema')
def step_impl(context):
    pass    
    
def salva_participantes(participantes):
    for participante in participantes:
        participante.save()   
