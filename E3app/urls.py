from django.urls import path
from .views import inicio, proveedor, cliente, venta

urlpatterns = [
    path('', inicio, name="inicio"),
    path('proveedores/', proveedor, name="proveedores"),
    path('formproveedores/', proveedor, name="formproveedores"),
    path('clientes/', cliente, name="clientes"),
    path('ventas/', venta, name="ventas"),

]