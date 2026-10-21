from django.contrib import admin
from .models import Generos, Filmes
from rest_framework.authtoken.models import Token

#Admin para o modelo Generos: mostra o nome e permite pesquisa
@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ['nome']  #Colunas exibidas na listagem
    search_fields = ['nome']  #Campos pesquisáveis

#Admin para o modelo Filmes: exibe os campos principais e adiciona filtros
@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'genero', 'ano_lancamento', 'duracao']  #Colunas da listagem
    search_fields = ['titulo', 'descricao']  #Campos pesquisáveis
    list_filter = ['ano_lancamento', 'genero']  #Filtros laterais

admin.site.register(Token)
