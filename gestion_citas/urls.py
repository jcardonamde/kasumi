# gestion_citas/urls.py

from django.urls import path
from .views import (
    CitaListView, 
    CitaCreateView, 
    CitaUpdateView, 
    CitaDeleteView
)

app_name = 'gestion_citas'

urlpatterns = [
    # CRUD de Citas
    path('', CitaListView.as_view(), name='lista_citas'),
    path('crear/', CitaCreateView.as_view(), name='crear_cita'),
    path('<int:pk>/editar/', CitaUpdateView.as_view(), name='editar_cita'),
    path('<int:pk>/eliminar/', CitaDeleteView.as_view(), name='eliminar_cita'),
]