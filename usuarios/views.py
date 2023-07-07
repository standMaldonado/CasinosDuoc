from django.shortcuts import render, redirect
from .models import USUARIO,CIUDAD

def eliminar(request):
    return render(request, 'eliminaruser.html')

def modificar(request):
    return render(request, 'modificaruser.html')

def ver(request):
    return render(request, 'veruser.html')

def agregaruser(request):
    if request.method is not "POST":
        ciudades=CIUDAD.objects.all();
        context={'nombre_ciudad':ciudades}
        return render(request,'agregaruser.html',context)
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        contra=request.POST["contra"]
        nombre_ciudad=request.POST["nombre_ciudad"]
        saldo=request.POST["saldo"]
        correo=request.POST["correo"]
        activo="1"

        objCiudad=CIUDAD.objects.get(id_ciudad = nombre_ciudad)
        obj=USUARIO.objects.create(rut=rut,
                                nombre=nombre,
                                contra=contra,
                                id_ciudad=objCiudad,
                                saldo=saldo,
                                correo=correo,
                                activo=1)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'agregaruser.html',context)
    
    
