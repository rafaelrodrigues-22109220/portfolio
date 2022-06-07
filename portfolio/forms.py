from django.forms import ModelForm

from .models import Post, Cadeira, Projeto

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


        

