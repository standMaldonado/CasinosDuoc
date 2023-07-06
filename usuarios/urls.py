from django.db import models
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns= [
    path('eliminar/', views.eliminar, name='eliminar'),
    path('ver/', views.ver, name='ver'),
    path('modificar/', views.modificar, name='modificar'),
    path('agregar/', views.agregar, name='agregar'),
]