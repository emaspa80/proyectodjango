from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    producto=models.CharField(max_length=20) #Para definir remera, buzo o cualquier otro
    precio=models.IntegerField()
    oferta=models.BooleanField() #Para activar o no si esta en oferta
    valid=models.BooleanField()  #Para activar o no el producto en la vista

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=11)
