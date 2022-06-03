from django.contrib import admin

from.models import Pessoa, Post, PontuacaoQuizz
# Register your models here.

admin.site.register(Pessoa)

admin.site.register(Post)

admin.site.register(PontuacaoQuizz)
