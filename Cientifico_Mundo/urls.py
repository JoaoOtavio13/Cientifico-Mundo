from django.urls import path
from Cientifico_Mundo.views import *

urlpatterns = [
    path('', index, name='index'),
    path('projeto/', projeto, name='projeto'),
    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('editar_usuario/<int:id>/', editar_usuario, name='editar_usuario'),
    path('exclusao_usuario/<int:id>/', exclusao_usuario, name='exclusao_usuario'),
    path('perfil/', perfil, name='perfil'),
    path('cadastro_projeto/', cadastro_projeto, name='cadastro_projeto'),
    path('editar_projeto/<int:id>/', editar_projeto, name='editar_projeto'),
    path('exclusao_projeto/<int:id>/', exclusao_projeto, name='exclusao_projeto'),
]