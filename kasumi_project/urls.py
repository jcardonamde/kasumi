"""kasumi_project URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Apps
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('usuarios/', include(('gestion_usuarios.urls', 'gestion_usuarios'), namespace='gestion_usuarios')),
    path('gestion/servicios/', include('gestion_servicios.urls')), 
    path('gestion/citas/', include('gestion_citas.urls')), 
    path('gestion/agenda/', include('gestion_agenda.urls')), 
    path('gestion/especialistas/', include('gestion_especialistas.urls')),
    path('gestion/clientes/', include('gestion_clientes.urls')),
    path('reportes/', include('reportes.urls',)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)