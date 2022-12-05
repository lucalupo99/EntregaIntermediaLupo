from django.shortcuts import render
from django.http import HttpResponse
from Peluqueria.models import *
from Peluqueria.forms import *
# Create your views here.

def turno(request):
    turno1=Turno(nombre="Luca", apellido="Lupo", Telefono=25252525)
    
    turno.save()
    cadena_txt="Turno Reservado: "+turno.nombre+" "+turno.apellido+" "+str(turno.telefono)
    return HttpResponse(cadena_txt)


def inicio(request):
    return render (request, "Peluqueria/inicio.html")

def usuarios(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nomb=informacion["nombre"]
            apel=informacion["apellido"]
            mail=informacion["email"]
            doc=informacion["documento"]
            clientito=Cliente(nombre=nomb, apellido=apel, email=mail, documento=doc)
            clientito.save()
            return render (request, "Peluqueria/inicio.html")

    else:
        formulario=ClienteForm()

    return render (request, "Peluqueria/usuarios.html", {"form":formulario})

def contacto(request):
    if request.method=="POST":
        form=ProductoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nomb=informacion["nombre"]
            prod=informacion["producto"]
            marc=informacion["marca"]
            tel=informacion["telefono"]
            productito=Producto(nombre=nomb, producto=prod, marca=marc, telefono=tel)
            productito.save()
        return render (request, "Peluqueria/inicio.html")
    else:
        formulario=ProductoForm()

    return render (request, "Peluqueria/contacto.html", {"form":formulario})




def turnosFormulario(request):
    if request.method=="POST":
        form=TurnoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombrecito=informacion["nombre"]
            apellidito=informacion["apellido"]
            telefonito=informacion["Telefono"]
        
            turno1=Turno(nombre=nombrecito, apellido=apellidito, Telefono=telefonito)
            turno1.save()
            return render (request, "Peluqueria/inicio.html")
    else:
        formulario=TurnoForm()

    return render (request, "Peluqueria/turnosFormulario.html", {"form":formulario})



def busquedaProductos(request):
    return render(request, "Peluqueria/busquedaProductos.html")

def buscar(request):
    if request.GET["producto"]:

        producto=request.GET["producto"]

        marca=Producto.objects.filter(producto__icontains=producto)
        return render(request, "Peluqueria/resultadosBusqueda.html", {"producto":producto, "marca":marca })
    else:
        return render(request, "Peluqueria/busquedaProductos.html", {"mensaje":"Porfavor Ingrese un producto"})
    