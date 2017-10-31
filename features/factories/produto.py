import factory
from app.models import *


class ProdutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Produto
        django_get_or_create = ('descricao', 'valorProduto', 'valorComissao', 'modalidade', 'quantidadeDisponivel', 'dataSorteio')