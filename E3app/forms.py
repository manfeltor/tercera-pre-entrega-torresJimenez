from django import forms

class FormProveedor(forms.Form):

    nombre = forms.CharField(max_length=100)
    rubro = forms.CharField(max_length=20)
    mail = forms.EmailField(empty_value="vacio")

class FormProveedor(forms.Form):

    nombre = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=20)
    activo = forms.BooleanField()

class FormVenta(forms.Form):
    articulo = forms.CharField(max_length=300)
    monto = forms.IntegerField()