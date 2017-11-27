from rest_framework import routers, serializers, viewsets
from .models import *



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class TipoBolaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBolao
        fields = ('url','codigo', 'modalidade','cotas','valorBolao', 'valorTaxa')

class ModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidade
        fields = ('url','descricao')

class BolaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bolao
        fields = ('url', 'dataSorteio', 'cotasDisponiveis', 'identificador','tipoBolao')

class VendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venda
        fields = ('url', 'dataHoraVenda', 'guiche', 'produto','bolao','vendedor')

class GuicheSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guiche
        fields = ('url', 'numero', 'descricao', 'codigoCEF')
        
class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ('url', 'descricao', 'valorProduto', 'valorComissao','modalidade','quantidadeDisponivel','dataSorteio')