# gestion_servicios/urls.py

from django.urls import path
from .views import (
    ServicioListView, 
    ServicioCreateView, 
    ServicioUpdateView, 
    ServicioDeleteView
)

app_name = 'gestion_servicios'

urlpatterns = [
    # CRUD de Servicios
    path('servicios/', ServicioListView.as_view(), name='lista_servicios'),
    path('servicios/crear/', ServicioCreateView.as_view(), name='crear_servicio'),
    path('servicios/<int:pk>/editar/', ServicioUpdateView.as_view(), name='editar_servicio'),
    path('servicios/<int:pk>/eliminar/', ServicioDeleteView.as_view(), name='eliminar_servicio'),
]