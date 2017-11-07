#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import *
from datetime import date
import datetime
from django.forms import ModelMultipleChoiceField, ModelChoiceField
from django.contrib.admin import widgets 


class formUser(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required' : 'True', 'max_length' : '30', 'placeholder' : 'Senha', 'render_value':'False', 'class' : 'form-control'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'password': ('Senha:'),
        }

class formFuncionario(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        fields = '__all__'
        exclude = ['dataContratacao','dataDemissao']


class formModalidade(forms.ModelForm):
    
    class Meta:
        model = Modalidade
        fields = '__all__'
        

class formTipoBolao(forms.ModelForm):
    
    class Meta:
        model = TipoBolao
        fields = '__all__'


class formProduto(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = '__all__'
        
        
class formBolao(forms.ModelForm):
    

    class Meta:
        model = Bolao
        fields = '__all__'
        exclude = ['dataCriacao']
        
        
class formGuiche(forms.ModelForm):
    
    class Meta:
        model = Guiche
        fields = '__all__'
        

class formTipoFuncionario(forms.ModelForm):
    
    class Meta:
        model = TipoFuncionario
        fields = '__all__'