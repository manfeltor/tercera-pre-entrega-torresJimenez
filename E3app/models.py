from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    rubro = models.CharField(max_length=20)
    mail = models.EmailField(null= True, blank= True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=20)
    activo = models.BooleanField()

class Venta(models.Model):
    articulo = models.CharField(max_length=300)
    monto = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

