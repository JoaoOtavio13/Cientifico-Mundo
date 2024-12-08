from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

# Listagem de artigos
def index(request):
    projetos=Projeto.objects.all()
  
    # paginação
    paginator=Paginator(projetos, 6)
    page=request.GET.get('page')
    projetos=paginator.get_page(page)
    
    context={
        'projetos':projetos,
    }
    return render(request, 'index.html',context)

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        # autenticação
        usuario=authenticate(username=username, password=password)
        
        if usuario is not None:
            login(request, usuario) # loga usuario
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method=='POST':
        form=UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('index')
    else:
        form=UsuarioForm()
    context={
        'form':form
    }
    return render(request, 'cadastro.html',context)

#crud do usuario
def cadastro_usuario(request):
    if request.method=='POST':
        form=UsuarioForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('index')
    else:
        form=UsuarioForm()
    context={
        'form':form
    }
    return render(request, 'cadastro.html',context)

@login_required
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

@login_required
def exclusao_usuario(request, id):
    usuario=Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('index')

#crud do artigo
@login_required
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

@login_required
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

@login_required
def exclusao_projeto(request, id):
    projeto=Projeto.objects.get(id=id)
    projeto.delete()
    return redirect('perfil')

#pagina do artigo
def projeto(request,projeto_id):
    projeto=Projeto.objects.get(id=projeto_id)
    context={
        'projeto':projeto
    }
    return render(request, 'projeto.html',context)

#perfil
@login_required
def perfil(request):
    usuario = Usuario.objects.get(id=request.user.id)
    projetos = Projeto.objects.filter(usuario=request.user).order_by('titulo')  # Ordena alfabeticamente por título
    
    # Aplicação do filtro
    projetos_filter = ProjetoFilterForm(request.GET, queryset=projetos)  # Passe o QuerySet inicial
    
    # Obtenha o QuerySet filtrado diretamente e ordenado
    projetos_filtrados = projetos_filter.qs.order_by('titulo')  # Ordena novamente após filtrar

    # Paginação
    paginator = Paginator(projetos_filtrados, 3)
    page = request.GET.get('page')
    projetos = paginator.get_page(page)

    # Contexto para renderização
    context = {
        'usuario': usuario,
        'projetos': projetos,
        'projetos_filter': projetos_filter
    }
    return render(request, 'perfil.html', context)


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
