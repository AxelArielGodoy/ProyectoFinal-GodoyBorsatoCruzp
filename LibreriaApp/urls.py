from django.urls import path

from accounts.views import login
from .views import crear_libro, inicio, blog, contacto, acerca_de

urlpatterns = [
    path('', inicio, name='inicio'),
    path('blog/', blog, name='blog'),
    path('contacto/', contacto, name='contacto'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('crear_libro/', crear_libro, name='crear_libro'),
]