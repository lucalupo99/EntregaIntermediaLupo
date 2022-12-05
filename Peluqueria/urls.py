from django.urls import path
from Peluqueria.views import *

urlpatterns = [
    path('usuarios/', usuarios, name='usuarios'), 
    path('contacto/', contacto, name='contacto'),
    path("", inicio),
    path("turnosFormulario/", turnosFormulario, name="turnosFormulario"),
    path("busquedaProductos/", busquedaProductos, name="busquedaProductos"),
    path("buscar/", buscar, name="buscar"),

]