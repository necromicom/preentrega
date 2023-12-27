
from django.urls import path
from aplicacion.views import leer_autor, index
urlpatterns = [
    path("autor/", leer_autor),
    path("", index)
]
