from django.contrib import admin
from .models import Pedidos, Productos, Clientes
# Register your models here.
admin.site.register(Pedidos)
admin.site.register(Productos)
admin.site.register(Clientes)
