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
from django.utils import timezone
from datetime import datetime,timedelta
from rest_framework import viewsets,permissions
from .serializers import *


@csrf_protect
@login_required

def relatorio_home(request):
    return render(request, 'home.html')
    
@csrf_protect
@login_required
def realiza_venda_bolao(request):
    boloes = Bolao.objects.all()
    boloes_validos = boloes.filter(cotasDisponiveis__gte=1,dataSorteio__gte=datetime.now())
    return render(request, 'realiza_venda_bolao.html', {'boloes': boloes_validos})    

@csrf_protect
@login_required
def realiza_venda_produto(request):
    produtos = Produto.objects.all()
    produtos_validos = produtos.filter(dataSorteio__gte=datetime.now())
    return render(request, 'realiza_venda_produto.html', {'produtos': produtos_validos})    
    
    
@csrf_protect
@login_required
def venda_bolao(request, pk):
    bolao = get_object_or_404(Bolao, pk=pk)
    bolao.vende_cota()
    Venda.objects.create(vendedor=request.user, bolao=bolao, dataHoraVenda=datetime.now(), guiche=Guiche.objects.get(numero='1'))
    bolao.save()
    return redirect('/realiza_venda_bolao')

@csrf_protect
@login_required
def venda_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.vende()
    Venda.objects.create(vendedor=request.user, produto=produto, dataHoraVenda=datetime.now(), guiche=Guiche.objects.get(numero='1'))
    produto.save()
    return redirect('/realiza_venda_produto')


@csrf_protect
@login_required
def lista_venda(request):
    yesterday = date.today() - timedelta(1)
    ##LIMITA ACESSO VENDAS POR USUARIO LOGADO
    vendas = Venda.objects.all()
    vendas = Venda.objects.filter(dataHoraVenda__gte=yesterday)
    return render(request, 'lista_venda.html', {'vendas': vendas})

@csrf_protect
@login_required
def lista_venda_por_dias(request, quantidade_dias):
    periodo = date.today() - timedelta(int(quantidade_dias))
    ##LIMITA ACESSO VENDAS POR USUARIO LOGADO
    vendas = Venda.objects.all()
    if request.user.funcionario.is_admin():
        vendas = Venda.objects.filter(dataHoraVenda__gte=periodo)
    else:
        vendas = Venda.objects.filter(vendedor=request.user,dataHoraVenda__gte=periodo)
    return render(request, 'lista_venda.html', {'vendas': vendas})


@csrf_protect
@login_required
def lista_venda_por_vendedor(request, pk):
    user = get_object_or_404(User, pk=pk)    
    ##LIMITA ACESSO VENDAS POR USUARIO LOGADO
    vendas = Venda.objects.all()
    vendas = Venda.objects.filter(vendedor=pk)
    return render(request, 'lista_venda.html', {'vendas': vendas})

@csrf_protect
@login_required
def lista_vendedores(request):
    funcionarios = Funcionario.objects.all()
    funcionarios = Funcionario.objects.filter(tipoFuncionario=TipoFuncionario.objects.get(descricao='Vendedor'))
    return render(request, 'lista_vendedores.html', {'funcionarios': funcionarios})


##### Views de Cadastros #####

def cadastro_funcionario(request):
    if request.method == 'POST':
        form_user = FormUser(request.POST)
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
            Funcionario.objects.create(user=user, tipoFuncionario=tipo_funcionario, nome=nome, sobrenome=sobrenome, dataContratacao=datetime.now(),salario=0)
            return HttpResponseRedirect(request.POST.get('next'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form_user = FormUser()

    return render(request, 'cadastro_funcionario.html', { 'form_user': form_user} )
    
    
@csrf_protect
@login_required
def cadastro_modalidade(request):
    if request.method == 'POST':
        form_modalidade = FormModalidade(request.POST)
        if form_modalidade.is_valid():
            form_modalidade.cleaned_data['descricao']
            form_modalidade.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_modalidade = FormModalidade()
            
    return render(request, 'cadastro_modalidade.html', { 'form_modalidade': form_modalidade} )


@csrf_protect
@login_required
def cadastro_tipo_bolao(request):
    if request.method == 'POST':
        form_tipo_bolao = FormTipoBolao(request.POST)
        if form_tipo_bolao.is_valid():
            form_tipo_bolao.cleaned_data['codigo']
            form_tipo_bolao.cleaned_data['modalidade']
            form_tipo_bolao.cleaned_data['cotas']
            form_tipo_bolao.cleaned_data['valorBolao']
            form_tipo_bolao.cleaned_data['valorTaxa']
            form_tipo_bolao.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_tipo_bolao = FormTipoBolao()
            
    return render(request, 'cadastro_tipo_bolao.html', { 'form_tipo_bolao': form_tipo_bolao} )


@csrf_protect
@login_required
def cadastro_produto(request):
    if request.method == 'POST':
        form_produto = FormProduto(request.POST)
        if form_produto.is_valid():
            form_produto.cleaned_data['descricao']
            form_produto.cleaned_data['valorProduto']
            form_produto.cleaned_data['valorComissao']
            form_produto.cleaned_data['modalidade']
            form_produto.cleaned_data['quantidadeDisponivel']
            form_produto.cleaned_data['dataSorteio']
            form_produto.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_produto = FormProduto()
            
    return render(request, 'cadastro_produto.html', { 'form_produto': form_produto} )


def cadastro_bolao(request):
    if request.method == 'POST':
        form_bolao = FormBolao(request.POST)
        if form_bolao.is_valid():
            form_bolao.cleaned_data['dataSorteio']
            tipoBolao = form_bolao.cleaned_data['tipoBolao']
            bolao = form_bolao.save(commit=False)
            bolao.cotasDisponiveis = tipoBolao.cotas
            bolao.save()
            
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_bolao = FormBolao()
            
    return render(request, 'cadastro_bolao.html', { 'form_bolao': form_bolao} )


@csrf_protect
@login_required
def cadastro_guiche(request):
    if request.method == 'POST':
        form_guiche = FormGuiche(request.POST)
        if form_guiche.is_valid():
            form_guiche.cleaned_data['numero']
            form_guiche.cleaned_data['descricao']
            form_guiche.cleaned_data['codigoCEF']
            form_guiche.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_guiche = FormGuiche()
            
    return render(request, 'cadastro_guiche.html', { 'form_guiche': form_guiche} )


@csrf_protect
@login_required
def cadastro_tipo_funcionario(request):
    if request.method == 'POST':
        form_tipo_funcionario = FormTipoFuncionario(request.POST)
        if form_tipo_funcionario.is_valid():
            form_tipo_funcionario.cleaned_data['descricao']
            form_tipo_funcionario.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form_tipo_funcionario = FormTipoFuncionario()
            
    return render(request, 'cadastro_tipo_funcionario.html', { 'form_tipo_funcionario': form_tipo_funcionario} )





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
def editar_funcionario(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form_user = FormUser(request.POST,instance=user)
        if form_user.is_valid():
            user = form_user.save(commit=False)
            user.first_name = form_user.cleaned_data['first_name']
            user.last_name = form_user.cleaned_data['last_name']
            user.username = form_user.cleaned_data['username']
            user.email = form_user.cleaned_data['email']
            user.password = form_user.cleaned_data['password']
            user.save()
            
            messages.success(request, 'Os dados foram atualizados com sucesso.')
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_user = FormUser(instance=user)

    return render(request, 'editar_funcionario.html', { 'form_user': form_user, 'user':user} )

@csrf_protect
@login_required
def editar_usuario(request, pk):
    #user = get_object_or_404(User, pk=pk)
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form_funcionario = FormFuncionario(request.POST,instance=funcionario)
        if form_funcionario.is_valid():
            #funcionario = form_funcionario.save(commit=False)
            form_funcionario.cleaned_data['tipoFuncionario']
            form_funcionario.cleaned_data['cpf']
            form_funcionario.cleaned_data['rg']
            form_funcionario.cleaned_data['ctps']
            form_funcionario.cleaned_data['salario']
            funcionario.save()
            
            messages.success(request, 'Os dados foram atualizados com sucesso.')
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_funcionario = FormFuncionario(instance=funcionario)

    return render(request, 'editar_usuario.html', { 'form_funcionario': form_funcionario, 'funcionario':funcionario} )


    
    
@csrf_protect
@login_required
def editar_modalidade(request, pk):
    modalidade = get_object_or_404(Modalidade, pk=pk)
    if request.method == 'POST':
        form_modalidade = FormModalidade(request.POST,instance=modalidade)
        if form_modalidade.is_valid():
            modalidade = form_modalidade.save(commit=False)
            modalidade.descricao = form_modalidade.cleaned_data['descricao']
            modalidade.save()
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_modalidade = FormModalidade(instance=modalidade)

    return render(request, 'editar_modalidade.html', { 'form_modalidade': form_modalidade, 'modalidade':modalidade} )


@csrf_protect
@login_required
def editar_tipo_bolao(request, pk):
    tipo_bolao = get_object_or_404(TipoBolao, pk=pk)
    if request.method == 'POST':
        form_tipo_bolao = FormTipoBolao(request.POST,instance=tipo_bolao)
        if form_tipo_bolao.is_valid():
            tipo_bolao = form_tipo_bolao.save(commit=False)
            tipo_bolao.codigo = form_tipo_bolao.cleaned_data['codigo']
            tipo_bolao.modalidade = form_tipo_bolao.cleaned_data['modalidade']
            tipo_bolao.cotas = form_tipo_bolao.cleaned_data['cotas']
            tipo_bolao.valorBolao = form_tipo_bolao.cleaned_data['valorBolao']
            tipo_bolao.valorTaxa = form_tipo_bolao.cleaned_data['valorTaxa']
            tipo_bolao.save()
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_tipo_bolao = FormTipoBolao(instance=tipo_bolao)

    return render(request, 'editar_tipo_bolao.html', { 'form_tipo_bolao': form_tipo_bolao, 'tipoBolao':tipo_bolao} )

@csrf_protect
@login_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form_produto = FormProduto(request.POST,instance=produto)
        if form_produto.is_valid():
            produto = form_produto.save(commit=False)
            produto.descricao = form_produto.cleaned_data['descricao']
            produto.valorProduto = form_produto.cleaned_data['valorProduto']
            produto.valorComissao = form_produto.cleaned_data['valorComissao']
            produto.modalidade = form_produto.cleaned_data['modalidade']
            produto.quantidadeDisponivel = form_produto.cleaned_data['quantidadeDisponivel']
            produto.dataSorteio = form_produto.cleaned_data['dataSorteio']
            produto.save()
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_produto = FormProduto(instance=produto)

    return render(request, 'editar_produto.html', { 'form_produto': form_produto, 'produto':produto} )


@csrf_protect
@login_required
def editar_bolao(request, pk):
    bolao = get_object_or_404(Bolao, pk=pk)
    if request.method == 'POST':
        form_bolao = FormBolao(request.POST,instance=bolao)
        if form_bolao.is_valid():
            bolao = form_bolao.save(commit=False)
            bolao.identificador = form_bolao.cleaned_data['identificador']
            bolao.dataSorteio = form_bolao.cleaned_data['dataSorteio']
            bolao.tipoBolao = form_bolao.cleaned_data['tipoBolao']
            bolao.save()
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_bolao = FormBolao(instance=bolao)

    return render(request, 'editar_bolao.html', { 'form_bolao': form_bolao, 'bolao':bolao} )

@csrf_protect
@login_required
def editar_guiche(request, pk):
    guiche = get_object_or_404(Guiche, pk=pk)
    if request.method == 'POST':
        form_guiche = FormGuiche(request.POST,instance=guiche)
        if form_guiche.is_valid():
            guiche = form_guiche.save(commit=False)
            guiche.numero = form_guiche.cleaned_data['numero']
            guiche.descricao = form_guiche.cleaned_data['descricao']
            guiche.codigoCEF = form_guiche.cleaned_data['codigoCEF']
            guiche.save()
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_guiche = FormGuiche(instance=guiche)

    return render(request, 'editar_guiche.html', { 'form_guiche': form_guiche, 'guiche':guiche} )

@csrf_protect
@login_required
def editar_tipo_funcionario(request, pk):
    tipoFuncionario = get_object_or_404(TipoFuncionario, pk=pk)
    if request.method == 'POST':
        form_tipo_funcionario = FormTipoFuncionario(request.POST,instance=tipoFuncionario)
        if form_tipo_funcionario.is_valid():
            tipoFuncionario = form_tipo_funcionario.save(commit=False)
            tipoFuncionario.descricao = form_tipo_funcionario.cleaned_data['descricao']
            tipoFuncionario.save()
            return HttpResponseRedirect(request.POST.get('next'))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form_tipo_funcionario = FormTipoFuncionario(instance=tipoFuncionario)

    return render(request, 'editar_tipo_funcionario.html', { 'form_tipo_funcionario': form_tipo_funcionario, 'tipoFuncionario':tipoFuncionario} )



##DELETAR
@csrf_protect
@login_required
def deletar_funcionario(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('/lista_funcionario')


@csrf_protect
@login_required
def deletar_modalidade(request, pk):
    modalidade = get_object_or_404(Modalidade, pk=pk)
    modalidade.delete()
    return redirect('/lista_modalidade')

@csrf_protect
@login_required
def deletar_tipo_bolao(request, pk):
    tipoBolao = get_object_or_404(TipoBolao, pk=pk)
    tipoBolao.delete()
    return redirect('/lista_tipo_bolao')

@csrf_protect
@login_required
def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('/lista_produto')

@csrf_protect
@login_required
def deletar_bolao(request, pk):
    bolao = get_object_or_404(Bolao, pk=pk)
    bolao.delete()
    return redirect('/lista_bolao')

@csrf_protect
@login_required
def deletar_guiche(request, pk):
    guiche = get_object_or_404(Guiche, pk=pk)
    guiche.delete()
    return redirect('/lista_guiche')
    
    
@csrf_protect
@login_required
def deletar_tipo_funcionario(request, pk):
    tipoFuncionario = get_object_or_404(TipoFuncionario, pk=pk)
    tipoFuncionario.delete()
    return redirect('/lista_tipo_funcionario')



#API VIEWS
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ModalidadesViewSet(viewsets.ModelViewSet):
    
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer

class TipoBoloesViewSet(viewsets.ModelViewSet):
    queryset = TipoBolao.objects.all()
    serializer_class = TipoBolaoSerializer

class BoloesViewSet(viewsets.ModelViewSet):
    boloes = Bolao.objects.all()
    queryset = boloes.filter(cotasDisponiveis__gte=1,dataSorteio__gte=datetime.now())
    serializer_class = BolaoSerializer

class VendasViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class GuichesViewSet(viewsets.ModelViewSet):
    queryset = Guiche.objects.all()
    serializer_class = GuicheSerializer
    
class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer