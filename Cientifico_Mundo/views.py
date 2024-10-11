from django.shortcuts import render

# Create your views here.

#listagem de artigos
def index(request):
    return render(request, 'index.html')

#pagina do artigo
def artigo(request):
    return render(request, 'artigo.html')

#pagina de cadastro de usuario
def cadastro(request):
    return render(request, 'cadastro.html')

#pagina de login
def login(request):
    return render(request, 'login.html')

#adicionar artigo
def adicionar_artigo(request):
    return render(request, 'adicionar_artigo.html')