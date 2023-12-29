from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Autor, Libro
from aplicacion.forms import FormularioLibros, FormAutor, Formdevuelto


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

def autor(request):
    if request.method == "POST":
        autorform = FormAutor(request.POST)
        if autorform.is_valid():
            datos = autorform.cleaned_data
            nombre = datos.get("nombre")
            apellido = datos.get("aprllido")
            autor1 = Autor(nombre=nombre, apellido=apellido)
            autor1.save
            return render(request, "index.html")
    else:
        autorform = FormAutor()        

    return render(request, "autor.html", {'form': autorform})


def buscar (request):
    if request.method == "GET":
        buscar = request.GET.get("nombre")
        if buscar is None:
            return HttpResponse("No esta")
        
        name = Libro.objects.filter(buscar__icontains=buscar)

        texto = {
            "paginas": name,
            "nombre": buscar
        }
        return render(request, "buscar2.html", texto)
    
    return render(request, "buscar.html")