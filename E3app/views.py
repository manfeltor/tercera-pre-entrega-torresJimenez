from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import FormProveedor, FormCliente, FormVenta
from .models import Proveedor, Cliente, Venta

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
            ven = Proveedor(nombre = data["nombre"], rubro = data["rubro"], mail = data["mail"])
            ven.save()
            instance = Proveedor.objects.all()
            context = {"instances": instance}

            return render(req, "proveedor.html", context)
        
        else:
            print (formulario1)
            return render(req, "inicio.html")
    
    else:
        
        formulario1 = FormProveedor()
        return render(req, "formproveedor.html", {"formulario1": formulario1})
    
def formCliente(req):

    print (req.method)

    if req.method == 'POST':

        formulario1 = FormCliente(req.POST)

        if formulario1.is_valid():

            data = formulario1.cleaned_data
            ven = Cliente(nombre = data["nombre"], ciudad = data["ciudad"], activo = data["activo"])
            ven.save()
            instance = Cliente.objects.all()
            context = {"instances": instance}

            return render(req, "cliente.html", context)

        else:
            print (formulario1)
            return render(req, "inicio.html")
    
    else:
        
        formulario1 = FormCliente()
        return render(req, "formcliente.html", {"formulario1": formulario1})
    
def formVentas(req):

    print (req.method)

    if req.method == 'POST':

        formulario1 = FormVenta(req.POST)

        if formulario1.is_valid():

            data = formulario1.cleaned_data
            ven = Venta(articulo = data["articulo"], monto = data["monto"])
            ven.save()
            instance = Venta.objects.all()
            context = {"instances": instance}

            return render(req, "venta.html", context)
        
        else:
            print (formulario1)
            return render(req, "inicio.html")
    
    else:
        
        formulario1 = FormVenta()
        return render(req, "formventa.html")
    
def buscar(req: HttpRequest):

        if req.GET["nombre"]:

            prv = req.GET["nombre"]
            
            instance = Proveedor.objects.filter(nombre__contains=prv)
            context = {"instances": instance}
            return render(req, "resultadosBusqueda.html", context)
        
        else:

            return HttpResponse(f"Debe agregar una camada")
    
def busquedaProveedor(req):

    return render(req, "busquedaproveedor.html")


