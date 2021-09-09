from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicial'),
    path('sobre_nos/', views.sobre, name='sobre'),
    path('bases/', views.bases, name='bases'),
    path('fechar_pag/', views.fechar, name='fechar'),
]
