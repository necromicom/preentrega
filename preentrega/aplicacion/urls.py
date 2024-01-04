
from django.urls import path
from aplicacion.views import autor, index, libro, devuelto, buscar
urlpatterns = [
    path("autor/", autor, name="autor"),
    path("", index, name="inicio"),
    path("libro/", libro, name="libro"),
    path("devuelto/", devuelto, name="devuelto"),
    path("buscar/", buscar, name="buscar"),
]
