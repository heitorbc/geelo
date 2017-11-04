import factory
from app.models import *



class FuncionarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Funcionario
        django_get_or_create = ('user', 'tipoFuncionario', 'nome', 'sobrenome', 'cpf', 'rg', 'ctps', 'dataContratacao', 'dataDemissao', 'salario')