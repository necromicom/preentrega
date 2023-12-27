from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=(20))
    apellido = models.CharField(max_length=(20))
    def __str__(self):
        return f"{self.nombre}--{self.apellido}"
    
class Libro(models.Model):
    nombre = models.CharField(max_length=(50))
    paginas = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} y tiene {self.paginas} paginas" 



class Devuelto(models.Model):
    nombre = models.CharField(max_length=20)
    devuelto = models.BooleanField()
    def __str__(self):
        return f"{self.nombre}--{self.devuelto}"