from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactoForm, AltaClienteForm, AltaClienteFormModel
from .models import Productos
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}     
    return render(request, 'app_t_virtual/index.html', context)

def gracias(request, nombre):
    return HttpResponse(f"Hola, <b>{nombre}</b> gracias por estar aqui")

def remeras(request):
    
    context = {}
    
    listado = Productos.objects.filter(producto = 'Remera').order_by('producto')
    
    context['listado_remeras'] = listado

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

def listar_productos(request):
    context = {}
    
    listado = Productos.objects.all().order_by('producto')
    
    context['listado_productos'] = listado

    return render(request, 'app_t_virtual/listar_productos.html', context)

def contacto(request): 
    context = {
        'form': ContactoForm
    }
    return render(request, 'app_t_virtual/contacto.html', context)
    
@login_required(login_url='/admin/login/')
def alta_clientes(request):
    context = {}
    if request.method == "POST":
        form = AltaClienteFormModel(request.POST)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.SUCCESS, 'Formulario completado con éxito')
            return redirect("index")
    else:
        form = AltaClienteFormModel()

    context["form"] = form
    return render(request, 'app_t_virtual/alta_clientes.html', context)


# Create your views here.


