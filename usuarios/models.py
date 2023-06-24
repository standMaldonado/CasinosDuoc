from django.db import models

# Create your models here.
class USUARIO(models.Model):
    rut = models.IntegerField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=30,blank=False,null=False)
    contra = models.CharField(max_length=30,blank=False,null=False)
    id_ciudad = models.ForeignKey('Ciudad',on_delete=models.CASCADE, db_column='idciudad')
    def __str__(self):
        return str(self.rut)

class CIUDAD(models.Model):
    id_ciudad  = models.AutoField(db_column='idciudad', primary_key=True) 
    nombre     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)

    

