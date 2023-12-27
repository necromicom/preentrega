from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Autor



def leer_autor(request):
    return render(request, "autor.html")

def index(request):
    return render(request, "index.html")