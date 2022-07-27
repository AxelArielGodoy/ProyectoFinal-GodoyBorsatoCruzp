from django.conf import settings
from django.urls import path
from .views import login, perfil, new_account, editar_perfil, ChangePasswordView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login, name='login'),
    path('new_account/', new_account, name='new_account'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar_contra', ChangePasswordView.as_view(), name='cambiar_contra'),
]


urlpatterns += static(settings.MEDIA_ROOT, docuement_root=settings.MEDIA_ROOT,)