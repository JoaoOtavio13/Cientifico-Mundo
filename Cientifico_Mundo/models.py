from django.db import models

# Create your models here.
class Ocupacao(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    ocupacao=models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    imagem=models.ImageField(upload_to='usuarios', null=True, blank=True)
    def __str__(self):
        return self.nome
    
class Comentario(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto=models.TextField()
    def __str__(self):
        return self.texto