from django.shortcuts import render

def eliminar(request):
    return render(request, 'eliminaruser.html')

def modificar(request):
    return render(request, 'modificaruser.html')

def agregar(request):
    return render(request, 'agregaruser.html')

def ver(request):
    return render(request, 'veruser.html')