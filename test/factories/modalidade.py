import factory
from app.models import *


class ModalidadeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Modalidade
        django_get_or_create = ('descricao')