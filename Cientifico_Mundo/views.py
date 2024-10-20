from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as login_django
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
        print(form.errors)
        if form.is_valid():
            Usuario.objects.create_user(**form.cleaned_data)
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
        form=UsuarioEditForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            usuario.set_password(request.POST.get('password'))
            return redirect('index') 
    else:
        form=UsuarioEditForm(instance=usuario)
    context={
        'form':form
    }
    return render(request, 'editar.html',context)

def exclusao_usuario(request, id):
    usuario=Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('index')

#perfil
def perfil(request):
    context={
        'usuario': Usuario.objects.get(id=request.user.id)    
}
    return render(request, 'perfil.html',context)

#crud do artigo
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
def projeto(request,projeto_id):
    projeto=Projeto.objects.get(id=projeto_id)
    context={
        'projeto':projeto
    }
    return render(request, 'projeto.html',context)

#pagina de login
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        usuario=authenticate(username=username, password=password)
        if usuario:
            login_django(request, usuario)
            return redirect('index')
    return render(request, 'login.html')
