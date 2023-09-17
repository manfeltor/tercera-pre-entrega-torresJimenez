from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormProveedor, FormCliente, FormVenta
from .models import Proveedor, Cliente, Venta
from django.db import IntegrityError

# Create your views here.

def proveedor(req):

    all_instances = Proveedor.objects.all()
    return render(req, 'venta.html', {'instances': all_instances})

def cliente(req):

    all_instances = Cliente.objects.all()
    return render(req, 'cliente.html', {'instances': all_instances})

def venta(req):

    all_instances = Venta.objects.all()
    return render(req, 'venta.html', {'instances': all_instances})

def inicio(req):

    return render(req, "inicio.html")

def formProveedor(req):

    print (req.method)

    if req.method == 'POST':

        formulario1 = FormProveedor(req.POST)

        if formulario1.is_valid():

            data = formulario1.cleaned_data
            prv = Proveedor(nombre = data["nom"], rubro = data["rub"], mail = ["mail"])
            prv.save()

            return render(req, "proveedor.html")
    
    else:
        
        formulario1 = FormProveedor()
        return render (req, "formproveedor.html", {})
    
def formCliente(req):

    print (req.method)

    if req.method == 'POST':

        formulario1 = FormCliente(req.POST)

        if formulario1.is_valid():

            data = formulario1.cleaned_data
            prv = Cliente(nombre = data["nom"], ciudad = data["city"], activo = ["active"])
            prv.save()

            return render(req, "cliente.html")
    
    else:
        
        formulario1 = FormProveedor()
        return render (req, "formcliente.html", {})
    
def formVentas(req):

    print (req.method)

    if req.method == 'POST':

        formulario1 = FormVenta(req.POST)

        if formulario1.is_valid():

            data = formulario1.cleaned_data
            ven = Venta(articulo = data["articulo"], monto = data["monto"])
            ven.save()

            return render(req, "venta.html")
        
        else:
            print (formulario1)
            return render(req, "inicio.html")
    
    else:
        
        formulario1 = FormVenta()
        return render(req, "formventa.html", {"formulario1": formulario1})