from django.urls import path
from Cientifico_Mundo.views import *

urlpatterns = [
    path('', index, name='index'),
    path('artigo/', artigo, name='artigo'),
    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('editar_usuario/<int:id>/', editar_usuario, name='editar_usuario'),
    path('perfil/', perfil, name='perfil'),
    path('exclusao_usuario/<int:id>/', exclusao_usuario, name='exclusao_usuario'),
    path('cadastro_artigo/', cadastro_artigo, name='cadastro_artigo'),
    path('editar_artigo/<int:id>/', editar_artigo, name='editar_artigo'),
    path('exclusao_artigo/<int:id>/', exclusao_artigo, name='exclusao_artigo'),
]