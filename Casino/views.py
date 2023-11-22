from django.shortcuts import render, redirect
from usuarios.models import USUARIO
from mecanico.models import Producto
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

def menu(request):
    productos = Producto.objects.all()
    return render(request, 'menu.html', {'productos': productos})
def mi_perfil(request):
    return render(request, 'mi_perfil.html')

def somos(request):
    return render(request, 'somos.html')

def soporte(request):
    return render(request, 'soporte.html')


