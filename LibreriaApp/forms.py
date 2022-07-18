from django import forms

class FormularioLibro(forms.Form):
    titulo = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)
    fecha_lanzamiento = forms.IntegerField()
    idioma = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=500)
    precio = forms.IntegerField()