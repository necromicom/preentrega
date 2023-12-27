
from django.urls import path
from aplicacion.views import leer_autor
urlpatterns = [
    path("autor/", leer_autor),
]
