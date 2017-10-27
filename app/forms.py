#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import *
from datetime import date
import datetime
from django.forms import ModelMultipleChoiceField, ModelChoiceField
from django.contrib.admin import widgets 


class Form_User(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required' : 'True', 'max_length' : '30', 'placeholder' : 'Senha', 'render_value':'False', 'class' : 'form-control'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'password': ('Senha:'),
        }


class Form_Modalidade(forms.ModelForm):
    
    class Meta:
        model = Modalidade
        fields = '__all__'
        

class Form_TipoBolao(forms.ModelForm):
    
    class Meta:
        model = TipoBolao
        fields = '__all__'


class Form_Produto(forms.ModelForm):
    
    
    class Meta:
        model = Produto
        fields = '__all__'
        
        
class Form_Guiche(forms.ModelForm):
    
    class Meta:
        model = Guiche
        fields = '__all__'