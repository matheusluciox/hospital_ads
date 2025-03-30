from django.contrib import admin
from .models import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de endereços no painel de administração.
    list_display = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep', 'data_criacao', 'data_atualizacao') 

    # Permite pesquisar endereços pelos campos especificados (como logradouro, bairro, cidade e cep).
    search_fields = ('rua', 'bairro', 'cidade', 'cep')

    # Adiciona filtros laterais para facilitar a filtragem por estado e cidade.
    list_filter = ('estado', 'cidade')