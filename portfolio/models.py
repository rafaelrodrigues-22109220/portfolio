from django.db import models


# Create your models here.

class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures/', blank=True)

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300)
    imagem = models.ImageField(upload_to="pictures/")

    def __str__(self):
        return self.titulo

class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    descricao = models.TextField(default=0)
    assunto = models.CharField(max_length=10)
    docente = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pontuacao = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to="pictures/")

    def __str__(self):
        return self.nome

class Post(models.Model):
    autor = models.CharField(max_length=30)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=90)
    descricao = models.CharField(max_length=500)


    def __str__(self):
        return self.titulo


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=30)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
