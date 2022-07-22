from django.urls import path

from accounts.views import login
from .views import inicio,crear_post, contacto, acerca_de, buscar_post


urlpatterns = [
    path('', inicio, name='inicio'),
    path('blog/', crear_post, name='crear_post'),
    path('contacto/', contacto, name='contacto'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('loggin', login),
    path('buscar/', buscar_post, name='buscar_post'),
]