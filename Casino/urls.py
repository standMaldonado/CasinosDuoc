from django.db import models
from django.urls import path
from . import views

app_name = 'Casino'
urlpatterns= [
    path('', views.index, name='index'),
    path("productos/", views.menu, name='menu'),
    path('Servicios/', views.mi_perfil, name='mi_perfil'),
    path("somos/", views.somos, name='somos'),
    path("soporte/", views.soporte, name='soporte'),
    
]