from django.shortcuts import render
from .models import Produto

# Create your views here.
def index(request):
    return render(request, 'appTest/index.html', {})

def sobre(request):
    return render(request, 'appTest/sobre.html', {})

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})