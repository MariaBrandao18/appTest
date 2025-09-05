from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'appTest/index.html', {})

def sobre(request):
    return render(request, 'appTest/sobre.html', {})