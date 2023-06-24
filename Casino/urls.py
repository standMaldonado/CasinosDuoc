from django.db import models
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path("menu/", views.menu, name='menu'),
    path('mi_perfil/', views.mi_perfil, name='mi_perfil'),
    path("somos/", views.somos, name='somos'),
    path("soporte/", views.soporte, name='soporte'),
]