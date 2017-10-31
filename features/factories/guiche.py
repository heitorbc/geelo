import factory
from app.models import *




class GuicheFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Guiche
        django_get_or_create = ('numero', 'descricao', 'codigoCEF')