from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html',{})

def restaurantes(request):
    return render(request,'restaurantes.html',{})

@login_required
def registroRestaurante(request):
    return render(request,'registroRestaurante.html',{})