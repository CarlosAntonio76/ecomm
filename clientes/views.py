from django.shortcuts import render
from django.http import HttpResponse


def cliente(request):
    return HttpResponse('<h1>Ecommerce CAJB - 2021 / Clientes</h1>')
