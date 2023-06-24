from django.db import models

class COMIDA(models.Model):
    id_comida = models.AutoField(db_column='IdComida', primary_key=True)
    nombre = models.CharField(max_length=30,blank=False,null=False)
    descripcion = models.CharField(max_length=200,blank=False,null=False)
    def __str__(self):
        return str(self.nombre)

class BEBIDA(models.Model):
    id_bebida = models.AutoField(db_column='IdBebida', primary_key=True)
    nombre = models.CharField(max_length=30,blank=False,null=False)
    descripcion = models.CharField(max_length=200,blank=False,null=False)
    def __str__(self):
        return str(self.nombre)
    
    
    


