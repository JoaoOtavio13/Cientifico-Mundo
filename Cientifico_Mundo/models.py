from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager  
# Create your models here.
class Ocupacao(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Usuário precisa de um nome de usuário')
        if not email:
            raise ValueError('Usuário precisa de um email')
        usuario = Usuario(
            username=(username),
            email=(email), **extra_fields,
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    def create_superuser(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Usuário precisa de um nome de usuário')
        usuario = Usuario(
            username=(username), **extra_fields
        )
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.is_active = True
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    ocupacao=models.ForeignKey(Ocupacao, on_delete=models.CASCADE, null=True, blank=True)
    imagem=models.ImageField(upload_to='usuarios', null=True, blank=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['idade']
    objects = UsuarioManager()
    date_joined = None
    def __str__(self):
        return self.nome
    
class Comentario(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto=models.TextField()
    def __str__(self):
        return self.texto

class Ocupaçao(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

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
    validacao = models.ForeignKey(Validacao, on_delete= models.CASCADE)
    imagem = models.ImageField(upload_to='capas/')
    orientador = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.titulo