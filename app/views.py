# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.shortcuts import render


@csrf_protect
@login_required
def relatorio_home(request):
    
    return render(request, 'home.html')
    
    
def cadastro_funcionario(request):
    if request.method == 'POST':
        form_user = Form_User(request.POST)
        if form_user.is_valid():
            nome = form_user.cleaned_data['first_name']
            sobrenome = form_user.cleaned_data['last_name']
            username = form_user.cleaned_data['username']
            email = form_user.cleaned_data['email']
            senha = form_user.cleaned_data['password']
            user = User.objects.create_user(username, email, senha)
            user.last_name=sobrenome
            user.first_name=nome
            user.save()
            tipo_funcionario = TipoFuncionario.objects.get(descricao='Vendedor')
            Funcionario.objects.create(user=user, tipo_funcionario=tipo_funcionario)
            return HttpResponseRedirect(request.POST.get('next'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form_user = Form_User()

    return render(request, 'cadastro_usuario.html', { 'form_user': form_user} )
    
    
@csrf_protect
@login_required
def cadastro_modalidade(request):
    if request.method == 'POST':
        form_modalidade = Form_Modalidade(request.POST)
        if form_modalidade.is_valid():
            descricao = form_modalidade.cleaned_data['descricao']
            form_modalidade.save()
            return HttpResponseRedirect(request.POST.get('next'))
        
    else:
        form_modalidade = Form_Modalidade()
            
    return render(request, 'cadastro_modalidade.html', { 'form_modalidade': form_modalidade} )
    
    
@csrf_protect
@login_required
def lista_modalidade(request):
    modalidades = Modalidade.objects.all()
    return render(request, 'lista_modalidade.html', {'modalidades': modalidades})


@csrf_protect
@login_required
def cadastro_tipo_bolao(request):
    if request.method == 'POST':
        form_tipo_bolao = Form_TipoBolao(request.POST)
        if form_tipo_bolao.is_valid():
            codigo = form_tipo_bolao.cleaned_data['codigo']
            modalidade = form_tipo_bolao.cleaned_data['modalidade']
            cotas = form_tipo_bolao.cleaned_data['cotas']
            valorBolao = form_tipo_bolao.cleaned_data['valorBolao']
            valorTaxa = form_tipo_bolao.cleaned_data['valorTaxa']
            form_tipo_bolao.save()
            return HttpResponseRedirect(request.POST.get('next'))
        
    else:
        form_tipo_bolao = Form_TipoBolao()
            
    return render(request, 'cadastro_tipo_bolao.html', { 'form_tipo_bolao': form_tipo_bolao} )
    
    
@csrf_protect
@login_required
def lista_tipo_bolao(request):
    tipoboloes = TipoBolao.objects.all()
    return render(request, 'lista_tipo_bolao.html', {'tipoboloes': tipoboloes})