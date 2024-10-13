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

@admin.register(Validação)
class ValidaçãoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituição']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'titulo', 'introducao', 'objetivo', 'metodologia', 'resultados', 'conclusao', 'validacao', 'imagem', 'orientador']



