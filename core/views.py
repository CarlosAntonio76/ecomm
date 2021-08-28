from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}
    return render(request, 'home/index.html', dicionario_contexto)
