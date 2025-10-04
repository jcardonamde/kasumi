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
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
