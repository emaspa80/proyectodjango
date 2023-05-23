from django.db import models

# Create your models here.
class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    talle=models.CharField(max_length=4,null=True)
    producto=models.CharField(max_length=20) #Para definir remera, buzo o cualquier otro
    precio=models.IntegerField()
    oferta=models.BooleanField() #Para activar o no si esta en oferta
    valid=models.BooleanField()  #Para activar o no el producto en la vista
    pedido = models.ManyToManyField(Pedidos) # Muchos a muchos pedidos y productos

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=11)
    dni=models.IntegerField(null=True)
    pedidos = models.ForeignKey(Pedidos, on_delete=models.CASCADE, null=True) # muchos a uno pedidos a clientes
