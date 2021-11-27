from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from django.views.generic import CreateView, ListView
#from core.models import Funcionario
from .models import Funcionario

def index(request):
    dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}
    return render(request, 'home/index.html', dicionario_contexto)

def sobre(request):
    textoe = {'msgneg': "testando..."}
    return render(request, 'home/index2.html', textoe)


def bases(request):
    textob = {'msgec': "testado..."}
    return render(request, 'home/index.bkp', textob)


def fechar(request):
    textoc = {'msgex': "testess..."}
    return render(request, 'home/fechar.html', textoc)


def inicial(request):
    Listar = Funcionario.objetos.all()
    return render(request, 'home/inicial.html', {'Listar': Listar})


@login_required(redirect_field_name='login')
def listarn(request):
    messages.info(request, 'Seja bem vindo(a)!')

    Listar = Funcionario.objetos.all()
    return render(request, 'home/listarn.html', {'Listar': Listar})

