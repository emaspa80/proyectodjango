from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gracias/<str:nombre>/', views.gracias, name="gracias"),
    path('remeras/', views.remeras, name="remeras"),#
    path('buzos/', views.buzos, name="buzos"),#
    path('ofertas/', views.ofertas, name="ofertas"),
    path('contacto/', views.contacto, name="contacto"),
    path('listar_productos/', views.listar_productos, name="listar_productos"),
    path('alta_clientes/', views.alta_clientes, name="alta_clientes"),
]
