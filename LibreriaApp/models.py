from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    # imagen= models.ImageField(upload_to='imagenes/')
    autor = models.CharField(max_length=30)
    fecha_lanzamiento = models.IntegerField()
    idioma = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    
    def __str__(self):
        return self.titulo