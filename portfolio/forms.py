from django.forms import ModelForm

from .models import Post, Cadeira, Projeto, Pessoa

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


        

