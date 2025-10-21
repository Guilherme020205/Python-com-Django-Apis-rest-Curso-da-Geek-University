# Importa o módulo de administração do Django
from django.contrib import admin

# Importa os modelos que você criou (Curso e Avaliacao)
from .models import Curso, Avaliacao


# === CONFIGURAÇÃO DO MODEL CURSO NO ADMIN ===

# O decorator @admin.register(Curso) registra o model "Curso" no painel admin
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # Define quais campos vão aparecer como colunas na listagem de cursos
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


# === CONFIGURAÇÃO DO MODEL AVALIACAO NO ADMIN ===

# Registra o model "Avaliacao" no painel admin
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na listagem de avaliações
    list_display = ('curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
