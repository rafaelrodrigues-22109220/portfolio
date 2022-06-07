from django.contrib import admin

from.models import Pessoa, Post, PontuacaoQuizz, Projeto, Cadeira
# Register your models here.

admin.site.register(Pessoa)

admin.site.register(Post)

admin.site.register(PontuacaoQuizz)

admin.site.register(Projeto)

admin.site.register(Cadeira)
