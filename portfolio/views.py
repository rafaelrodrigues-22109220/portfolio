import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Create your views here.
from django.shortcuts import render


from .forms import PostForm,CadeiraForm, ProjetoForm
from .models import Pessoa,Cadeira,Projeto, Post, PontuacaoQuizz



def home_page_view(request):
    agora = datetime.datetime.now()
    context = {
        'agora' : agora.year
    }
    return render(request, 'portfolio/home.html', context)


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)

def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def blog_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)

def new_post_page_view(request):
    #if not request.user.is_authenticated:
     #   return HttpResponseRedirect(reverse('portfolio:blog'))

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/new.html', context)

def edita_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edit.html', context)


def apaga_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def new_cadeira_page_view(request):
    #if not request.user.is_authenticated:
     #   return HttpResponseRedirect(reverse('portfolio:blog'))

    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form}

    return render(request, 'portfolio/new.html', context)

def edita_cadeira_view(request, post_id):
    post = Cadeira.objects.get(id=post_id)
    form = CadeiraForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edit.html', context)


def apaga_cadeira_view(request, post_id):
    Cadeira.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))


def new_projeto_page_view(request):
    #if not request.user.is_authenticated:
     #   return HttpResponseRedirect(reverse('portfolio:blog'))

    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/new.html', context)

def edita_projeto_view(request, post_id):
    post = Projeto.objects.get(id=post_id)
    form = ProjetoForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edit.html', context)


def apaga_projeto_view(request, post_id):
    Projeto.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

def pontuacao_quizz(request):
    score = 0
    lista = request.POST.getlist('ling')

    if request.POST['numero'] == '1991':
        score+=1

    if request.POST['nomeWeb'] == 'Tim Berners-Lee':
        score+=1

    if request.POST['html'] == 'html5':
        score+=1

    if 'python' in lista:
        score+=1

    if 'c++' in lista:
        if score > 0:
            score -= 1

    if 'html-css' in lista:
        score += 1

    if 'javaScript' in lista:
        score += 1

    return score

def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome = n, pontuacao = p)
        r.save()

    desenha_grafico_resultados(request)
    return render(request, 'portfolio/quizz.html')

def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all()
    pontuacao_sorted = sorted(pontuacoes, key=lambda objeto: objeto.pontuacao, reverse=False)
    listaNomes = []
    listapontuacao = []

    for person in pontuacao_sorted:
        listaNomes.append(person.nome)
        listapontuacao.append(person.pontuacao)

    plt.barh(listaNomes, listapontuacao)
    plt.savefig('portfolio/static/portfolio/images/graf.png', bbox_inches='tight')

def view_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def view_logout(request):
    logout(request)

    return render(request, 'portfolio/home.html', {
                'message': 'Foi desconetado.'
            })

