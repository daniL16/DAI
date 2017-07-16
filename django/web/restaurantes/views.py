from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from .forms import SearchForm, AddForm, DelForm

def index(request):
    return render(request,'index.html',{})

def restaurantes(request):
    return render(request,'restaurantes.html',{})

@login_required
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            restaurant = form.cleaned_data['restaurant']
            db = models.db
            data = db.restaurants.find({'name': restaurant})
            dic = {}
            b = []
            cuisine = " "
            name = " "
            dic['form'] = form
            for d in data:
                b.append(d['borough'])
                cuisine = d['cuisine']
                name = d['name']
            if name == " " and cuisine == " ":
                dic['message'] = "No se ha encontrado ningun restaurante con estos criterios"
            dic['restaurant'] = {'cuisine': cuisine,
                                 'borough': b,
                                 'name': name}
            return render(request, 'restaurante.html', dic)
    else:
        form = SearchForm()
    return render(request, 'restaurante.html', {'form': form})

@login_required
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            dic = {'name': form.cleaned_data['name'],
                   'borough': form.cleaned_data['borough'],
                   'cuisine': form.cleaned_data['cuisine']}
            db = models.db
            data = db.restaurants.insert(dic)

            return render(request, 'nuevoRest.html',
                          {'form': form,
                           'message': 'Restaurante registrado'})
    else:
        form = AddForm()
    return render(request, 'nuevoRest.html', {'form': form})

@login_required
def delete(request):
    if request.method == 'POST':
        form = DelForm(request.POST)
        if form.is_valid():
            dic = {'name': form.cleaned_data['name']}
            db = models.db
            db.restaurants.remove(dic)

            return render(request, 'delete.html',
                          {'form': form,
                           'message': 'Restaurante borrado correctamente'})
    else:
        form = DelForm()
    return render(request, 'delete.html', {'form': form})
