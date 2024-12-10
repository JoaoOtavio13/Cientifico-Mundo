from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    idade = forms.IntegerField(required=True, help_text='Digite sua idade')
    ocupacao = forms.ModelChoiceField(queryset=Ocupacao.objects.all(), required=True, help_text='Escolha uma ocupação')
    imagem = forms.ImageField(required=False, help_text='Escolha uma imagem')
    email = forms.EmailField(required=True, help_text='Digite seu email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classe form-control aos campos padão do UserCreationForm
        self.fields['username'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['email'].widget.attrs.update({ 'class': 'form-control'}) 
        self.fields['idade'].widget.attrs.update({'class': 'form-control'})
        self.fields['ocupacao'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagem'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})   
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'idade', 'ocupacao', 'imagem', 'password1', 'password2')

class UsuarioEditForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    idade = forms.IntegerField(
        required=True,
        help_text='Digite sua idade',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    ocupacao = forms.ModelChoiceField(
        queryset=Ocupacao.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    imagem = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classe form-control aos campos padão 
        self.fields['username'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['email'].widget.attrs.update({ 'class': 'form-control'}) 

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'idade', 'ocupacao', 'imagem')
     
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo','resumo','introducao','objetivo','metodologia','resultados','conclusao','validacao','imagem','orientador']

        widgets = {
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

import django_filters

class ProjetoFilterForm(django_filters.FilterSet):
    titulo = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Título',
        widget=forms.TextInput(attrs={'placeholder': 'Título do projeto', 'class': 'form-control'}),
        required=False
    )
    resumo = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Resumo',
        widget=forms.Textarea(attrs={'placeholder': 'Resumo do projeto', 'class': 'form-control'}),
        required=False
    )
    class Meta:
        model = Projeto  # Vincule explicitamente o modelo
        fields = ['titulo', 'resumo']
    
class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Deixe seu comentário...'
            }),
        }