from django.urls import path
from .views import inicio, tienda, blog, contacto, acerca_de, iniciar_sesion, registrarse

urlpatterns = [
    path('', inicio, name='inicio'),
    path('tienda/', tienda, name='tienda'),
    path('blog/', blog, name='blog'),
    path('contacto/', contacto, name='contacto'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', registrarse, name='registrarse'),
]