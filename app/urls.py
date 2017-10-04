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
    url(r'^cadastro_modalidade/$', cadastro_modalidade, name='cadastro_modalidade'),
    url(r'^cadastro_tipo_bolao/$', cadastro_tipo_bolao, name='cadastro_tipo_bolao'),
    url(r'^lista_modalidade/$', lista_modalidade, name='lista_modalidade'),
    url(r'^lista_tipo_bolao/$', lista_tipo_bolao, name='lista_tipo_bolao'),
]
