import factory
from app.models import *



class BolaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bolao
        django_get_or_create = ('identificador', 'dataCriacao', 'dataSorteio', 'tipoBolao', 'cotasDisponiveis')