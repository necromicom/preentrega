from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=(20))
    apellido = models.CharField(max_length=(20))
class Libro(models.Model):
    nombre = models.CharField(max_length=(50))
    paginas = models.IntegerField()