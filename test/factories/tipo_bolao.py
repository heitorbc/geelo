import factory
from app.models import *



class TipoBolaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TipoBolao
        django_get_or_create = ('codigo', 'modalidade', 'cotas', 'valorBolao', 'valorTaxa')









