from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('listar/', views.listarn, name='listarn'),
    #path('', views.index, name='index'),
    path('sobre_nos/', views.sobre, name='sobre'),
    path('bases/', views.bases, name='bases'),
    path('fechar_pag/', views.fechar, name='fechar'),
]
