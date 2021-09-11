from django.shortcuts import render
from django.http import HttpResponse

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
