#  hello/urls.py

from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('blog', views.blog_page_view, name='blog'),
    path('new_post', views.new_post_page_view, name ='new_post'),
    path('edit_post/<int:post_id>', views.edita_post_view ,name = 'edit_post'),
    path('apaga_post/<int:post_id>', views.apaga_post_view, name='apaga_post'),
    path('new_cadeira', views.new_cadeira_page_view, name ='new_cadeira'),
    path('edit_cadeira/<int:cadeira_id>', views.edita_cadeira_view ,name = 'edit_cadeira'),
    path('apaga_cadeira/<int:cadeira_id>', views.apaga_cadeira_view, name='apaga_cadeira'),
    path('new_projeto', views.new_projeto_page_view, name ='new_projeto'),
    path('edit_projeto/<int:projeto_id>', views.edita_projeto_view ,name = 'edit_projeto'),
    path('apaga_projeto/<int:projeto_id>', views.apaga_projeto_view, name='apaga_projeto'),
    path('quizz', views.quizz, name = 'quizz'),
    path('login', views.view_login, name='login'),
]
