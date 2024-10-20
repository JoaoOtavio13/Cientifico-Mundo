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

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }