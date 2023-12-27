
from django.urls import path
from aplicacion.views import leer_autor, index, libro, devuelto
urlpatterns = [
    path("autor/", leer_autor, name="autor"),
    path("", index, name="inicio"),
    path("libro/", libro, name="libro"),
    path("devuelto/", devuelto, name="devuelto"),
]
