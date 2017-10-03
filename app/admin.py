from django.contrib import admin

from .models import *

admin.site.register(TipoFuncionario)
admin.site.register(Funcionario)
admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Modalidade)
admin.site.register(Guiche)
admin.site.register(Bolao)
admin.site.register(TipoBolao)

