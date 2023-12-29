from django.contrib import admin

# Register your models here.
from aplicacion.models import Libro, Autor, Devuelto

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Devuelto)