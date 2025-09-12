from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('listar_produtos', views.listar_produtos, name='listar_produtos'),
]