from django.db import models


# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=500)

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
