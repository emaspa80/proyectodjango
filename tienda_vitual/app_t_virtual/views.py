from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 
from .forms import ContactoForm

def index(request):
    context = {}     
    return render(request, 'app_t_virtual/index.html', context)

def gracias(request, nombre):
    return HttpResponse(f"Hola, <b>{nombre}</b> gracias por estar aqui")

def remeras(request):
    
    listado_remeras = [
        {
            'nombre': 'Remera Totoro',
            'talle': 'S',
            'precio': 1500,
            'valid': False,
        },
        {
            'nombre': 'Remera Bowser',
            'talle': 'M',
            'precio': 1800,
            'valid': False,
        },
        {
            'nombre': 'Remera SEGA',
            'talle': 'L',
            'precio': 2000,
            'valid': False,
        },
    ]

    context = {
        #agregar las lineas con las demas listas buzos ...    
        'listado_remeras': listado_remeras
    }
    return render(request, 'app_t_virtual/remeras.html', context)

def buzos(request): 
    
    listado_buzos = [
        {
            'nombre': 'Buzo Akira',
            'talle': 'S',
            'precio': 1500,
            'valid': False,
        },
        {
            'nombre': 'Buzo Muten Roshi',
            'talle': 'M',
            'precio': 1800,
            'valid': False,
        },
        {
            'nombre': 'Buzo Strawberry',
            'talle': 'L',
            'precio': 2000,
            'valid': False,
        },
    ]

    context = {
        #agregar las lineas con las demas listas buzos ...    
        'listado_buzos': listado_buzos
    }
    return render(request, 'app_t_virtual/buzos.html', context)

def ofertas(request): 
        
    listado_ofertas = [
        {
            'nombre': 'Remera Tomy y Daly',
            'talle': 'S',
            'precio': 1000,
            'valid': False,
        },
        {
            'nombre': 'Remera Bowse',
            'talle': 'M',
            'precio': 1000,
            'valid': False,
        },
        {
            'nombre': 'Buzo Tokyo Revengers',
            'talle': 'L',
            'precio': 1500,
            'valid': False,
        },
    ]

    context = {
        #agregar las lineas con las demas listas buzos ...    
        'listado_ofertas': listado_ofertas
    }
    
    return render(request, 'app_t_virtual/ofertas.html', context)

def contacto(request): 
    context = {
        'form': ContactoForm
    }
    return render(request, 'app_t_virtual/contacto.html', context)



# Create your views here.


