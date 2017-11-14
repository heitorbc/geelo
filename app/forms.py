#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import *
from datetime import date
import datetime
from django.forms import ModelMultipleChoiceField, ModelChoiceField
from django.contrib.admin import widgets 
from django.forms import widgets


class FormUser(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required' : 'True', 'max_length' : '30', 'placeholder' : 'Senha', 'render_value':'False', 'class' : 'form-control'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'password': ('Senha:'),
        }

class FormFuncionario(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        fields = '__all__'
        exclude = ['user','nome','sobrenome','dataContratacao','dataDemissao']


class FormModalidade(forms.ModelForm):
    
    class Meta:
        model = Modalidade
        fields = '__all__'
        

class FormTipoBolao(forms.ModelForm):
    
    class Meta:
        model = TipoBolao
        fields = '__all__'


class FormProduto(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = '__all__'
        
        
class FormBolao(forms.ModelForm):
    dataSorteio = forms.DateTimeField(widget=forms.SplitDateTimeWidget())

    class Meta:
        model = Bolao
        fields = '__all__'
        exclude = ['dataCriacao','cotasDisponiveis']
        
        
class FormGuiche(forms.ModelForm):
    
    class Meta:
        model = Guiche
        fields = '__all__'
        

class FormTipoFuncionario(forms.ModelForm):
    
    class Meta:
        model = TipoFuncionario
        fields = '__all__'