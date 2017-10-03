#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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


class Guiche(models.Model):
    #Atributos        
    numero = models.IntegerField(null=False, blank=False)
    descricao = models.CharField(max_length=150)
    codigoCEF = models.IntegerField(null=False, blank=False)
    
    #ToString
    def __str__(self):
        return str(self.numero) + ' - ' + str(self.codigoCEF)
    

class Venda(models.Model):
    #Atributos
    vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='funcionario_venda')
    dataHoraVenda = models.DateTimeField(blank=True,verbose_name='Data/Hora da Venda')
    guiche = models.ForeignKey(Guiche, on_delete=models.CASCADE, related_name='guiche_venda')

    #Notações
    class Meta:
        verbose_name = ('Venda')
        verbose_name_plural = ('Vendas')
    
    #ToString
    def __str__(self):
        return self.vendedor.user.name + ' - ' + self.dataHoraVenda
        
        
        
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
    def __str__(self):
        return self.modalidade.descricao + ' - ' + self.dataSorteio

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
    def __str__(self):
        return self.codigo + " - R$" + str(self.valorBolao + self.valorTaxa)
        
        
class Bolao(models.Model):
    #Atributos
    dataCriacao = models.DateTimeField(blank=True,verbose_name='Data/Hora Criação')
    dataSorteio = models.DateTimeField(blank=True,verbose_name='Data/Hora Sorteio')
    tipoBolao = models.ForeignKey(TipoBolao, on_delete=models.CASCADE, related_name='tipoBolao_bolao')
    cotasDisponiveis = models.IntegerField(null=False, blank=False)
    
    #Notações
    class Meta:
        verbose_name = ('Bolão')
        verbose_name_plural = ('Bolões')
    
    #ToString
    def __str__(self):
        return self.cotasDisponiveis + ' - ' + self.dataSorteio