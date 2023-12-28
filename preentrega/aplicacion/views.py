from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Autor, Libro
from aplicacion.forms import FormularioLibros


def leer_autor(request):
    return render(request, "autor.html")

def index(request):
    return render(request, "index.html")

def libro(request):
    if request.method == "POST":
        libroform = FormularioLibros(request.POST)
        if  libroform.is_valid():
         datos = libroform.cleaned_data
         nomre = datos.get("nombre")
         paginas = datos.get("paginas")
         libro1 = Libro(nombre=nomre, paginas=paginas)
         libro1.save
        return render(request, "index.html")
    else:
        libroform = FormularioLibros()

    return render(request,"libro.html", {'form':libroform})

def devuelto(request):
    return render( request, "devuelto.html")