from django import forms

class FormularioLibros(forms.Form):
    nombre = forms.CharField(max_length=50)
    paginas = forms.IntegerField()


class FormAutor(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)


class Formdevuelto(forms.Form):
    nombre = forms.CharField(max_length=20)
    entrega = forms.BooleanField()