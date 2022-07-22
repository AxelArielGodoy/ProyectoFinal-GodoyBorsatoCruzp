from django.conf import settings
from django.urls import path
from .views import login
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]


urlpatterns += static(settings.MEDIA_ROOT, docuement_root=settings.MEDIA_ROOT,)