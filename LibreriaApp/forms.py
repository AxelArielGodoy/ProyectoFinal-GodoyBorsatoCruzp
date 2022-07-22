from django import forms
from ckeditor.fields import RichTextFormField

class FormularioLibro(forms.Form):
    titulo = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)
    fecha_lanzamiento = forms.IntegerField()
    idioma = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=500)
    precio = forms.IntegerField()
    
    
class FormularioPost(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=50)
    contenido = RichTextFormField()
    autor = forms.CharField(max_length=30)
    fecha_creacion = forms.IntegerField()
    # avatar = forms.ImageField(required=False)


class BusquedaPost(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)