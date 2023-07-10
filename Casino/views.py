from django.shortcuts import render, redirect
from usuarios.models import USUARIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def mi_perfil(request):
    return render(request, 'mi_perfil.html')

def somos(request):
    return render(request, 'somos.html')

def soporte(request):
    return render(request, 'soporte.html')


