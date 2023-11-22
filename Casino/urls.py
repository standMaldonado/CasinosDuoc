from django.db import models
from django.urls import path, include
from . import views

app_name = 'Casino'
urlpatterns= [
    path('', views.index, name='index'),
    path("productos/", views.menu, name='menu'),
    path('servicios/', views.mi_perfil, name='mi_perfil'),
    path('producto/<str:id_producto>/', views.somos, name='producto'),
    path("soporte/", views.soporte, name='soporte'),
<<<<<<< HEAD
    path('mecanico/', include('mecanico.urls'))
=======

>>>>>>> 0726d083560c666505aa1750c62b1bd581697481
    
]