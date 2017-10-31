from behave import *
from app.models import *
from app.views import *
from django.contrib.auth.models import User
from features.factories.tipo_funcionario import TipoFuncionarioFactory


@given(u'Eu possuo usuários cadastrados no sistema')
def given_user(context):
    user_heitor = UserFactory(username='heitor', email='heitorhbc@gmail.com', password='admin123456')
    user_thales = UserFactory(username='thales', email='thalescarreta@gmail.com', password='admin123456')
    user_root = UserFactory(username='admin', email='superuser@gmail.com', password='admin123456')
    
    lista_usuarios = [user_heitor, user_thales, user_root]
    
    salva_participantes(lista_usuarios)
    
    assert len(User.objects.all()) == 3


@given(u'Eu possuo tipo de funcionario cadastrado no sistema')
def given_tipo_funcionario(context):
    descricao = TipoFuncionarioFactory(descricao='Vendedor')

    descricao.save()

    assert len(TipoFuncionario.objects.all()) == 1
    
    
@given(u'Eu possuo funcionario cadastrado no sistema')
def given_funcionario(context):
    user_root = User.objects.get(username='admin')
    tipo_funcionario = TipoFuncionario.objects.get(nome='Vendedor')
    guiche = Guiche.objects.get(numero=01)
    
    funcionario = FuncionarioFactory(user=user_root.username, tipoFuncionario=tipo_funcionario , nome= , sobrenome= , cpf= , rg= , ctps= , dataContratacao= , dataDemissao= , salario= )
    
    assert len(Funcionario.objects.all()) == 1
    
    
@given(u'Eu possuo guiche cadastrado no sistema')
def given_guiche(context):
    numero = GuicheFactory(numero=01)
    descricao = GuicheFactory(descricao='Prioritario Jogos')
    codigoCEF =GuicheFactory(codigoCEF=191902)
     
    guiche = GuicheFactory(numero=numero, descricao=descricao, codigoCEF=codigoCEF)
    
def salva_participantes(participantes):
    for participante in participantes:
        participante.save()    