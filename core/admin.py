from django.contrib import admin
from .models import Funcionario


class PostAdmin(admin.ModelAdmin):
    list_display = ('codfunc','nome', 'sobrenome', 'cpf')
    list_display_links = ('codfunc', 'nome', 'cpf')
    #list_editable = ('cpf', 'nome')
    search_fields = ['codfunc', 'nome']


admin.site.register(Funcionario, PostAdmin)
