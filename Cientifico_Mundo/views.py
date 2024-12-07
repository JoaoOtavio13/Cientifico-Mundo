from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

# Listagem de artigos
def index(request):
    projetos=Projeto.objects.all()
    # projetos_filter=ProjetoFilterForm(request.GET or None)

    # filtragem
    # if projetos_filter.is_valid():
    #     if projetos_filter.cleaned_data['titulo']:
    #         projetos= projetos.filter(titulo__icontains=projetos_filter.cleaned_data['titulo'])
    #     if projetos_filter.cleaned_data['usuario']: 
    #         projetos= projetos.filter(usuario=projetos_filter.cleaned_data['usuario'])  
    #     if projetos_filter.cleaned_data['validacao']:   
    #         projetos= projetos.filter(validacao=projetos_filter.cleaned_data['validacao'])  
    #     if projetos_filter.cleaned_data['orientador']:   
    #         projetos= projetos.filter(orientador__icontains=projetos_filter.cleaned_data['orientador']) 
    #     if projetos_filter.cleaned_data['resumo']:   
    #         projetos= projetos.filter(resumo__icontains=projetos_filter.cleaned_data['resumo']) 
    #     if projetos_filter.cleaned_data['introducao']:
    #         projetos= projetos.filter(introducao__icontains=projetos_filter.cleaned_data['introducao'])
    #     if projetos_filter.cleaned_data['objetivo']:
    #         projetos= projetos.filter(objetivo__icontains=projetos_filter.cleaned_data['objetivo'])
    #     if projetos_filter.cleaned_data['metodologia']:
    #         projetos= projetos.filter(metodologia__icontains=projetos_filter.cleaned_data['metodologia'])
    #     if projetos_filter.cleaned_data['resultados']:
    #         projetos= projetos.filter(resultados__icontains=projetos_filter.cleaned_data['resultados'])
    #     if projetos_filter.cleaned_data['conclusao']:
    #         projetos= projetos.filter(conclusao__icontains=projetos_filter.cleaned_data['conclusao'])
    #     if projetos_filter.cleaned_data['imagem']:
    #         projetos= projetos.filter(imagem__icontains=projetos_filter.cleaned_data['imagem']) 
        
    # paginação
    paginator=Paginator(projetos, 3)
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
    usuario=Usuario.objects.get(id=request.user.id)
    context={
        'usuario': usuario     
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
