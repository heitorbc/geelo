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
from django.views.generic.edit import FormView
from datetime import datetime 


@csrf_protect
@login_required

def relatorio_home(request):
    
    return render(request, 'home.html')
    
    
    


##### Views de Cadastros #####


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
            tipoFuncionario = TipoFuncionario.objects.get(descricao='Vendedor')
            Funcionario.objects.create(user=user, tipoFuncionario=tipoFuncionario, nome=nome, sobrenome=sobrenome, dataContratacao=datetime.now(),salario=0)
            return HttpResponseRedirect(request.POST.get('next'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form_user = Form_User()

    return render(request, 'cadastro_funcionario.html', { 'form_user': form_user} )
    
    
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
def cadastro_produto(request):
    if request.method == 'POST':
        form_produto = Form_Produto(request.POST)
        if form_produto.is_valid():
            ### descrição ???
            descricao = form_produto.cleaned_data['descricao']
            valorProduto = form_produto.cleaned_data['valorProduto']
            valorComissao = form_produto.cleaned_data['valorComissao']
            modalidade = form_produto.cleaned_data['modalidade']
            quantidadeDisponivel = form_produto.cleaned_data['quantidadeDisponivel']
            ### cade a dataSorteio ???
            form_produto.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_produto = Form_Produto()
            
    return render(request, 'cadastro_produto.html', { 'form_produto': form_produto} )


def cadastro_bolao(request):
    if request.method == 'POST':
        form_bolao = Form_Bolao(request.POST)
        if form_bolao.is_valid():
            dataCriacao = form_bolao.cleaned_data['dataCriacao']
            dataSorteio = form_bolao.cleaned_data['dataSorteio']
            tipoBolao = TipoBolao.objects.get(descricao='tipoBolao_bolao')
            cotasDisponiveis = form_bolao.cleaned_data['cotasDisponiveis']
            form_bolao.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_bolao = Form_Bolao()
            
    return render(request, 'cadastro_bolao.html', { 'form_bolao': form_bolao} )


@csrf_protect
@login_required
def cadastro_guiche(request):
    if request.method == 'POST':
        form_guiche = Form_Guiche(request.POST)
        if form_guiche.is_valid():
            numero = form_guiche.cleaned_data['numero']
            descricao = form_guiche.cleaned_data['descricao']
            codigoCEF = form_guiche.cleaned_data['codigoCEF']
            form_guiche.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_guiche = Form_Guiche()
            
    return render(request, 'cadastro_guiche.html', { 'form_guiche': form_guiche} )


@csrf_protect
@login_required
def cadastro_tipo_funcionario(request):
    if request.method == 'POST':
        form_tipo_funcionario = Form_TipoFuncionario(request.POST)
        if form_guiche.is_valid():
            descricao = form_tipo_funcionario.cleaned_data['descricao']
            form_tipo_funcionario.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_tipo_funcionario = Form_TipoFuncionario()
            
    return render(request, 'cadastro_tipo_funcionario.html', { 'form_guiche': form_tipo_funcionario} )





##### Listagem de Modelos #####
    
    
@csrf_protect
@login_required
def lista_funcionario(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'lista_funcionario.html', {'funcionarios': funcionarios})
    
    
@csrf_protect
@login_required
def lista_modalidade(request):
    modalidades = Modalidade.objects.all()
    return render(request, 'lista_modalidade.html', {'modalidades': modalidades})


@csrf_protect
@login_required
def lista_tipo_bolao(request):
    tipoboloes = TipoBolao.objects.all()
    return render(request, 'lista_tipo_bolao.html', {'tipoboloes': tipoboloes})


@csrf_protect
@login_required
def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produto.html', {'produtos': produtos})


@csrf_protect
@login_required
def lista_bolao(request):
    boloes = Bolao.objects.all()
    return render(request, 'lista_bolao.html', {'boloes': boloes})
    
    
@csrf_protect
@login_required
def lista_guiche(request):
    guiches = Guiche.objects.all()
    return render(request, 'lista_guiche.html', {'guiches': guiches})


@csrf_protect
@login_required
def lista_tipo_funcionario(request):
    tipofuncionarios = TipoFuncionario.objects.all()
    return render(request, 'lista_tipo_funcionario.html', {'tipofuncionarios': tipofuncionarios})
    
    
    
    
##Editar
    
@csrf_protect
@login_required
def editar_modalidade(request, pk):
    modalidade = get_object_or_404(Modalidade, pk=pk)
    if request.method == 'POST':
        form_modalidade = Form_Modalidade(request.POST,instance=modalidade)
        if form_modalidade.is_valid():
            modalidade = form_modalidade.save(commit=False)
            modalidade.descricao = form_modalidade.cleaned_data['descricao']
            modalidade.save()
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_modalidade = Form_Modalidade(instance=modalidade)

    return render(request, 'editar_modalidade.html', { 'form_modalidade': form_modalidade, 'modalidade':modalidade} )
