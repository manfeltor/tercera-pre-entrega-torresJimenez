from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormProveedor
from .models import Proveedor

# Create your views here.

def proveedor(req):

    return render(req, "proveedor.html")

def cliente(req):

    return render(req, "cliente.html")

def venta(req):

    return render(req, "venta.html")

def inicio(req):

    return render(req, "inicio.html")

def formProveedor(req):

    print (req.method)

    if req.method == 'POST':

        formulario1 = FormProveedor(req.POST)

        if formulario1.is_valid():

            data = formulario1.cleaned_data
            prv = Proveedor(nombre = data["nom"], comision = data["com"])
            prv.save()

            return render(req, "proveedor.html")
    
    else:
        
        formulario1 = FormProveedor()
        return render (req, "formproveedor.html", {})