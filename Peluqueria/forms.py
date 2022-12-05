from django import forms

class TurnoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    Telefono = forms.IntegerField()

class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    documento= forms.IntegerField()

class ProductoForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    producto= forms.CharField(max_length=50)
    marca= forms.CharField(max_length=50)
    telefono= forms.IntegerField()