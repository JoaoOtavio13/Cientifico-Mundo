from django.urls import path
from Cientifico_Mundo.views import *

urlpatterns = [
    path('', index, name='index'),
    path('artigo/', artigo, name='artigo'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('adicionar_artigo/', adicionar_artigo, name='adicionar_artigo'),
]