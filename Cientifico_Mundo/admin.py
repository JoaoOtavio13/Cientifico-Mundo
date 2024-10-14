from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email','senha', 'ocupacao', 'imagem']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'texto']

@admin.register(Validacao)
class ValidacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituicao']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'titulo', 'introducao', 'objetivo', 'metodologia', 'resultados', 'conclusao', 'validacao', 'imagem', 'orientador']

@admin.register(Instituicao)
class InstituiçãoAdmin(admin.ModelAdmin):
    list_display = ['nome']