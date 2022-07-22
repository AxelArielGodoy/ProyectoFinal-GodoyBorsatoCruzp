from django.db import models
from ckeditor.fields import RichTextField

    
class Post(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    contenido = RichTextField()
    autor = models.CharField(max_length=30)
    fecha_creacion = models.IntegerField()
    
    def __str__(self):
        return f'El titulo es: {self.titulo}'
    
    
    
# imagen = models.ImageField(upload_to='avatres', null=True, blank=True)