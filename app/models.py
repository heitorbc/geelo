#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime


class TipoFuncionario(models.Model):
    #Atributos
    descricao = models.CharField(max_length=50)
    
    #ToString
    def __str__(self):
        return self.descricao


class Funcionario(models.Model):
    #Atributos
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipoFuncionario = models.ForeignKey(TipoFuncionario, on_delete=models.CASCADE, related_name='tipo_funcionario')
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=300)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=50)
    ctps = models.CharField(max_length=50)
    dataContratacao = models.DateTimeField(blank=True,verbose_name='Data de Contratação')
    dataDemissao = models.DateTimeField(null=True,blank=True,verbose_name='Data de Demissão')
    salario = models.DecimalField( max_digits=8, decimal_places=2)
    
    #Notações
    class Meta:
        verbose_name = ('Tipo Funcionário')
        verbose_name_plural = ('Funcionários')
    
    #ToString
    def __str__(self):
        return self.user.username
        
    #Demitir
    def demitir(self):
        self.dataDemissao = timezone.now()
        self.save()
    
    ##Verificar perfil de usuario é diferente de vendedor
    def is_admin(self):
        if self.tipoFuncionario==TipoFuncionario.objects.get(descricao='Vendedor'):
            return False
        else:
            return True


class Guiche(models.Model):
    #Atributos        
    numero = models.IntegerField(null=False, blank=False)
    descricao = models.CharField(max_length=150)
    codigoCEF = models.IntegerField(null=False, blank=False)
    
    #ToString
    def __str__(self):
        return str(self.numero) + ' - ' + str(self.codigoCEF)
    
    def getNumero(self):
        return str(self.numero)

        
        
class Modalidade(models.Model):
    #Atributos
    descricao = models.CharField(max_length=50)
    
    #Notações
    class Meta:
        verbose_name = ('Modalidade')
        verbose_name_plural = ('Modalidades')
    
    #ToString
    def __str__(self):
        return self.descricao
    
    

class Produto(models.Model):
    #Atributos
    descricao = models.CharField(max_length=50)
    valorProduto = models.DecimalField(max_digits=8, decimal_places=2)
    valorComissao = models.DecimalField(max_digits=8, decimal_places=2)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, related_name='produto_modalidade')
    quantidadeDisponivel = models.IntegerField(null=False, blank=False)
    dataSorteio = models.DateTimeField(blank=True,verbose_name='Data/Hora Sorteio')
    
    #Notações
    class Meta:
        verbose_name = ('Produto')
        verbose_name_plural = ('Produtos')
    
    #ToString
    def valor_total(self):
        return self.valorProduto + self.valorComissao
    
    #ToString
    def __str__(self):
        return self.modalidade.descricao + ' - R$ ' + str(self.valor_total())


    #Venda de Um Produto
    def vende(self):
        self.quantidadeDisponivel-=1


class TipoBolao(models.Model):
    #Atributos
    codigo = models.CharField(max_length=10)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, related_name='bolao_modalidade')
    cotas = models.IntegerField(null=False, blank=False)
    valorBolao = models.DecimalField(max_digits=8, decimal_places=2)
    valorTaxa = models.DecimalField(max_digits=8, decimal_places=2)
    
    #Notações
    class Meta:
        verbose_name = ('Tipo Bolão')
        verbose_name_plural = ('Tipo Bolões')
    
    #ToString
    def valor_total(self):
        return self.valorBolao + self.valorTaxa
        
    #Get Cotas
    def get_cotas(self):
        return self.cotas
    
    #ToString
    def __str__(self):
        return self.codigo + " - R$" + str(self.valorBolao + self.valorTaxa)
        
        
class Bolao(models.Model):
    #Atributos
    identificador = models.CharField(max_length=10)
    dataCriacao = models.DateTimeField(default=datetime.now(),blank=True,verbose_name='Data/Hora Criação')
    dataSorteio = models.DateTimeField(blank=True,verbose_name='Data/Hora Sorteio')
    tipoBolao = models.ForeignKey(TipoBolao, on_delete=models.CASCADE, related_name='tipoBolao_bolao')
    cotasDisponiveis = models.IntegerField(blank=True)
    
    #Notações
    class Meta:
        verbose_name = ('Bolão')
        verbose_name_plural = ('Bolões')
        
    #Venda de Uma cota
    def vende_cota(self):
        self.cotasDisponiveis-=1
        
    #Porcentagem vendida de bolao
    def porcentagem_vendida(self):
        porcentagem = 100-((self.cotasDisponiveis*100)/self.tipoBolao.cotas)
        return round(porcentagem, 2)
    
    #Retorna se tem menos de 2 cotas
    def acabando(self):
        return self.cotasDisponiveis < 3
    
    #ToString
    def __str__(self):
        return str(self.identificador) + ' - ' + str(self.tipoBolao.codigo) + ' - R$ ' + str(self.tipoBolao.valor_total())
        
        
        
class Venda(models.Model):
    #Atributos
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='funcionario_venda')
    bolao = models.ForeignKey(Bolao, blank=True,null=True, on_delete=models.CASCADE, related_name='bolao_venda')
    produto = models.ForeignKey(Produto, blank=True,null=True,on_delete=models.CASCADE, related_name='produto_venda')
    dataHoraVenda = models.DateTimeField(default=datetime.now(),blank=True,verbose_name='Data/Hora da Venda')
    guiche = models.ForeignKey(Guiche, on_delete=models.CASCADE, related_name='guiche_venda')

    #Notações
    class Meta:
        verbose_name = ('Venda')
        verbose_name_plural = ('Vendas')
    
    #ToString
    def __str__(self):
        return self.vendedor.username + ' - ' + str(self.dataHoraVenda)
        