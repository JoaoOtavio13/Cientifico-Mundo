from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Ocupacao(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    idade = models.IntegerField(null=True, blank=True)
    ocupacao=models.ForeignKey(Ocupacao, on_delete=models.CASCADE, null=True, blank=True)
    imagem=models.ImageField(upload_to='usuarios', null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario} em {self.projeto}"

class Instituicao(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Validacao(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.ForeignKey(Instituicao, on_delete= models.CASCADE) 
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    introducao = models.TextField()
    objetivo = models.TextField()
    metodologia = models.TextField()
    resultados = models.TextField()
    conclusao = models.TextField()
    validacao = models.ForeignKey(Validacao, on_delete= models.CASCADE, null=True, blank=True)
    imagem = models.ImageField(upload_to='capas/')
    orientador = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.titulo