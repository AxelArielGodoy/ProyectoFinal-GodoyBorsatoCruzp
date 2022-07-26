from django.urls import path

from accounts.views import login, new_account
from .views import eliminar_post, inicio,crear_post, contacto, buscar_post, editar_post, sobre_nosotros, ver_mas


urlpatterns = [
    path('', inicio, name='inicio'),
    path('blog/', crear_post, name='crear_post'),
    path('contacto/', contacto, name='contacto'),
    path('sobre_nosotros/', sobre_nosotros, name='sobre_nosotros'),
    path('loggin', login, name='login'),
    path('new_account/', new_account, name='new_account'),
    path('buscar/', buscar_post, name='buscar_post'),
    path('editar/<int:id>/', editar_post, name='editar_post'),
    path('eliminar/<int:id>/', eliminar_post, name='eliminar_post'),
    path('ver-mas/<int:id>/', ver_mas, name='ver_mas'),
]