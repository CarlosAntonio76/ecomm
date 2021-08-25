from django.shortcuts import render
from django.http import HttpResponse


def inicial(request):
    return HttpResponse('Testando - Aguarde...')
