import factory
from app.models import *


class TipoFuncionarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TipoFuncionario
        django_get_or_create = ('descricao')

    descricao = 'Vendedor'
