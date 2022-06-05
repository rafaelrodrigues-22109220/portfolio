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
    path('new',views.new_page_view, name ='new'),
    path('edit_post/<int:post_id>', views.edita_post_view ,name = 'edit_post'),
    path('apaga_post/<int:post_id>', views.apaga_post_view, name='apaga_post'),
    path('quizz', views.quizz, name = 'quizz'),
    path('login', views.view_login, name='login'),

]
