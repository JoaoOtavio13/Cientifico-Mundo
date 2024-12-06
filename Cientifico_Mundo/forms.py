from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','email','idade','password','ocupacao','imagem','username']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'ocupacao': forms.Select(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
         
class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome','email','idade','ocupacao','imagem','username']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'ocupacao': forms.Select(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
     
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumo': forms.Textarea(attrs={'class': 'form-control'}),
            'introducao': forms.Textarea(attrs={'class': 'form-control'}),
            'objetivo': forms.Textarea(attrs={'class': 'form-control'}),
            'metodologia': forms.Textarea(attrs={'class': 'form-control'}),
            'resultados': forms.Textarea(attrs={'class': 'form-control'}),
            'conclusao': forms.Textarea(attrs={'class': 'form-control'}),
            'validacao': forms.Select(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'orientador': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProjetoFilterForm(filter.Form): #'ProjetoFilterForm' é o nome da classe
    usuario = forms.ModelChoiceField( # Campo de seleção para o usuário
        queryset=Usuario.objects.all(),
        required=False,
        label='Usuário',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    titulo = forms.CharField( # Campo de texto para o título
        max_length=200,
        required=False,
        label='Título',
        widget=forms.TextInput(attrs={'playholder': 'Título do projeto', 'class': 'form-control'})
    )
    resumo = forms.CharField( # Campo de texto para o resumo
        required=False,
        label='Resumo',
        widget=forms.Textarea(attrs={'placeholder': 'Resumo do projeto', 'class': 'form-control'})
    )
    introducao = forms.CharField( # Campo de texto para a introdução
        required=False,
        label='Introdução',
        widget=forms.Textarea(attrs={'placeholder': 'Introdução do projeto', 'class': 'form-control'})
    )
    objetivo = forms.CharField( # Campo de texto para o objetivo
        required=False,
        label='Objetivo',
        widget=forms.Textarea(attrs={'placeholder': 'Objetivo do projeto', 'class': 'form-control'})
    )
    metodologia = forms.CharField( # Campo de texto para a metodologia
        required=False,
        label='Metodologia',
        widget=forms.Textarea(attrs={'placeholder': 'Metodologia do projeto', 'class': 'form-control'})
    )
    resultados = forms.CharField( # Campo de texto para os resultados
        required=False,
        label='Resultados',
        widget=forms.Textarea(attrs={'placeholder': 'Resultados do projeto', 'class': 'form-control'})
    )
    conclusao = forms.CharField( # Campo de texto para a conclusão
        required=False,
        label='Conclusão',
        widget=forms.Textarea(attrs={'placeholder': 'Conclusão do projeto', 'class': 'form-control'})
    )
    validacao = forms.ChoiceField( # Campo de seleção para a validação
        choices=Projeto.VALIDACAO_CHOICES,
        required=False,
        label='Validação',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }