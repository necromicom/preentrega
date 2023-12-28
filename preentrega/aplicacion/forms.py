from django import forms

class FormularioLibros(forms.Form):
    nombre = forms.CharField(max_length=50)
    paginas = forms.IntegerField()