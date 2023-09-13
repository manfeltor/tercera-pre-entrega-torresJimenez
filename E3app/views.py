from django.shortcuts import render

# Create your views here.

def proveedor(req):

    return render(req, "proveedor.html")

def cliente(req):

    return render(req, "cliente.html")

def venta(req):

    return render(req, "venta.html")

def inicio(req):

    return render(req, "inicio.html")