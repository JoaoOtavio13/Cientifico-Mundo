from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

#listagem de artigos
def index(request):
    projetos=Projeto.objects.all()
    context={
        'projetos':projetos
    }
    return render(request, 'index.html',context) 


#crud do usuario
def cadastro_usuario(request):
    if request.method=='POST':
        form=UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=UsuarioForm()
        context={
            'form':form
        }
    return render(request, 'cadastro.html',context)

def editar_usuario(request, id):
    usuario=Usuario.objects.get(id=id)
    if request.method=='POST':
        form=UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form=UsuarioForm(instance=usuario)
    context={
        'form':form
    }
    return render(request, 'cadastro.html',context)

def exclusao_usuario(request, id):
    usuario=Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('index')

#perfil
def perfil(request):
    return render(request, 'perfil.html')

#crud do artigo
# não está salvando
def cadastro_projeto(request):
    if request.method=='POST':
        form=ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ProjetoForm()
    context={
        'form':form
    }
    return render(request, 'adicionar_projeto.html',context)

def editar_projeto(request, id):
    projeto=Projeto.objects.get(id=id)
    if request.method=='POST':
        form=ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ProjetoForm(instance=projeto)
    context={
        'form':form
    }
    return render(request, 'adicionar_projeto.html',context)

def exclusao_projeto(request, id):
    projeto=Projeto.objects.get(id=id)
    projeto.delete()
    return redirect('index')

#pagina do artigo
def projeto(request):
    return render(request, 'projeto.html')
