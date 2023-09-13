from django.urls import path
from .views import inicio

urlpatterns = [
    path('', inicio, name="inicio"),
    path('proveedores/', inicio, name="proveedores"),
    path('clientes/', inicio, name="clientes"),
    path('ventas/', inicio, name="ventas"),

]