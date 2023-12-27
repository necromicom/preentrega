from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Autor, 



def leer_autor(request):
    texto = Autor()
    return render(request, "autor.html")
