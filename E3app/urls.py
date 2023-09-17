from django.urls import path
from .views import inicio, proveedor, cliente, venta, formProveedor, formCliente, formVentas

urlpatterns = [
    path('', inicio, name="inicio"),
    path('proveedores/', proveedor, name="proveedores"),
    path('formproveedores/', formProveedor, name="formproveedores"),
    path('clientes/', cliente, name="clientes"),
    path('formclientes/', formCliente, name="formcliente"),
    path('ventas/', venta, name="ventas"),
    path('formventas/', formVentas, name="formventas"),

]