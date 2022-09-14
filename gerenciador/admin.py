from django.contrib import admin
from .models import Categoria, Projeto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'titulo',
        'criado_em',
        'autor',
        'esta_publicado'
    )
    list_display_links = (
        'titulo',
        'criado_em',
    )
    ordering = '-id',

    list_editable = 'esta_publicado',