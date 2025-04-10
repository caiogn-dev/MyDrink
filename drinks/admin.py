from django.contrib import admin
from .models import Categoria, Ingrediente, Drink, Receita

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'descricao')
    search_fields = ('nome', 'tipo')
    list_filter = ('tipo',)

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_medida', 'preco_medio')
    search_fields = ('nome',)
    list_filter = ('unidade_medida',)

class ReceitaInline(admin.TabularInline):
    model = Receita
    extra = 1

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'tempo_preparo', 'dificuldade', 'data_criacao')
    search_fields = ('nome', 'descricao')
    list_filter = ('categoria', 'dificuldade', 'data_criacao')
    inlines = [ReceitaInline]

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('drink', 'ingrediente', 'quantidade')
    search_fields = ('drink__nome', 'ingrediente__nome')
    list_filter = ('drink', 'ingrediente')
