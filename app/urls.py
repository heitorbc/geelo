# -*- coding: utf-8 -*-
"""geelo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^home/$', relatorio_home, name='home'),
    url(r'^$', relatorio_home, name='home'),
    url(r'^cadastro_funcionario/$', cadastro_funcionario, name='cadastro_funcionario'),
    url(r'^cadastro_modalidade/$', cadastro_modalidade, name='cadastro_modalidade'),
    url(r'^cadastro_tipo_bolao/$', cadastro_tipo_bolao, name='cadastro_tipo_bolao'),
    url(r'^cadastro_produto/$', cadastro_produto, name='cadastro_produto'),
    url(r'^cadastro_bolao/$', cadastro_bolao, name='cadastro_bolao'),
    url(r'^cadastro_guiche/$', cadastro_guiche, name='cadastro_guiche'),
    url(r'^cadastro_tipo_funcionario/$', cadastro_tipo_funcionario, name='cadastro_tipo_funcionario'),
    
    
    url(r'^lista_funcionario/$', lista_funcionario, name='lista_funcionario'),
    url(r'^lista_modalidade/$', lista_modalidade, name='lista_modalidade'),
    url(r'^lista_tipo_bolao/$', lista_tipo_bolao, name='lista_tipo_bolao'),
    url(r'^lista_produto/$', lista_produto, name='lista_produto'),
    url(r'^lista_bolao/$', lista_bolao, name='lista_bolao'),
    url(r'^lista_guiche/$', lista_guiche, name='lista_guiche'),
    url(r'^lista_tipo_funcionario/$', lista_tipo_funcionario, name='lista_tipo_funcionario'),
    
    
    
    url(r'^funcionario/(?P<pk>\d+)/editar$', editar_funcionario, name='editar_funcionario'),
    url(r'^modalidade/(?P<pk>\d+)/editar$', editar_modalidade, name='editar_modalidade'),
    url(r'^tipo_bolao/(?P<pk>\d+)/editar$', editar_tipo_bolao, name='editar_tipo_bolao'),
    url(r'^produto/(?P<pk>\d+)/editar$', editar_produto, name='editar_produto'),
    url(r'^bolao/(?P<pk>\d+)/editar$', editar_bolao, name='editar_bolao'),
    url(r'^guiche/(?P<pk>\d+)/editar$', editar_guiche, name='editar_guiche'),
    url(r'^tipo_funcionario/(?P<pk>\d+)/editar$', editar_tipo_funcionario, name='editar_tipo_funcionario'),
    
    
    url(r'^funcionario/(?P<pk>\d+)/deletar', deletar_funcionario, name='deletar_funcionario'),
    url(r'^modalidade/(?P<pk>\d+)/deletar', deletar_modalidade, name='deletar_modalidade'),
    url(r'^tipo_bolao/(?P<pk>\d+)/deletar', deletar_tipo_bolao, name='deletar_tipo_bolao'),
    url(r'^produto/(?P<pk>\d+)/deletar', deletar_produto, name='deletar_produto'),
    url(r'^bolao/(?P<pk>\d+)/deletar', deletar_bolao, name='deletar_bolao'),
    url(r'^guiche/(?P<pk>\d+)/deletar', deletar_guiche, name='deletar_guiche'),
    url(r'^tipo_funcionario/(?P<pk>\d+)/deletar', deletar_tipo_funcionario, name='deletar_tipo_funcionario'),
]
