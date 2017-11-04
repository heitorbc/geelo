from behave import *
from app.models import *
from app.views import *
from django.contrib.auth.models import User
from .factories.user import UserFactory
from .factories.tipo_funcionario import TipoFuncionarioFactory
from .factories.guiche import GuicheFactory
from .factories.modalidade import ModalidadeFactory
from .factories.produto import ProdutoFactory


    
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
    user_root = User.objects.get(username='admin')
    tipo_funcionario = TipoFuncionario.objects.get(nome='Vendedor')
    
    funcionario = FuncionarioFactory(user=user_root.username, tipoFuncionario=tipo_funcionario, nome='Thales', sobrenome='C. Vescovi', cpf='147.231.177-22', rg='3.206.960', ctps='999-9' , dataContratacao='2017-08-12' , dataDemissao=True , salario=1500.00)
    
    funcionario.save()
    assert len(Funcionario.objects.all()) == 1
    


@given(u'Eu possuo guiche cadastrado no sistema')
def step_impl(context):
    guiche = GuicheFactory(numero=01, descricao='Prioritario Jogos', codigoCEF=191902)
    
    guiche.save()
    assert len(Guiche.objects.all()) == 1



@given(u'Eu possuo modalidade cadastrado no sistema')
def step_impl(context):
    descricao = ModalidadeFactory(descricao='Lotofacil')

    descricao.save()
    assert len(TipoFuncionario.objects.all()) == 1


@given(u'Eu possuo produto cadastrado no sistema')
def step_impl(context):
    produto = ProdutoFactory(descricao='Telesena', valorProduto=10.01, valorComissao=0.45, modalidade='Telesena', quantidadeDisponivel=150, dataSorteio=01/01/2017)
    
    produto.save()
    assert len(Modalidade.objects.all()) == 1


@given(u'Eu possuo tipo de bolao cadastrado no sistema')
def step_impl(context):
    pass


@given(u'Eu possuo bolao cadastrado no sistema')
def step_impl(context):
    pass




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
    
    



