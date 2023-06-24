from django.db import models
from django.urls import path
from . import views

urlpatterns= [
    path("", views.index),
    path("menu/", views.menu),
    path("mi_perfil/", views.mi_perfil),
    path("somos/", views.somos),
    path("soporte/", views.soporte),
]