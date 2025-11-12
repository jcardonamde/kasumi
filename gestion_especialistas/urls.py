# gestion_especialistas/urls.py (MODIFICADO)

from django.urls import path
from .views import (
    # Vistas de Especialista
    EspecialistaListView, EspecialistaCreateView, EspecialistaUpdateView, EspecialistaDeleteView,
    # Vistas de Horario Base
    HorarioBaseListView, HorarioBaseCreateView, HorarioBaseUpdateView, HorarioBaseDeleteView,
    # Vistas de Disponibilidad (✅ NUEVAS IMPORTACIONES)
    DisponibilidadListView, DisponibilidadCreateView, DisponibilidadUpdateView, DisponibilidadDeleteView
)

app_name = 'gestion_especialistas'

urlpatterns = [
    # CRUD de Especialistas
    path('', EspecialistaListView.as_view(), name='lista_especialistas'),
    path('crear/', EspecialistaCreateView.as_view(), name='crear_especialista'),
    path('<int:pk>/editar/', EspecialistaUpdateView.as_view(), name='editar_especialista'),
    path('<int:pk>/eliminar/', EspecialistaDeleteView.as_view(), name='eliminar_especialista'),
    
    # CRUD de Horarios Base
    path('horarios/', HorarioBaseListView.as_view(), name='lista_horarios'),
    path('horarios/crear/', HorarioBaseCreateView.as_view(), name='crear_horario'),
    path('horarios/<int:pk>/editar/', HorarioBaseUpdateView.as_view(), name='editar_horario'),
    path('horarios/<int:pk>/eliminar/', HorarioBaseDeleteView.as_view(), name='eliminar_horario'),
    
    # CRUD de Disponibilidad (✅ NUEVAS RUTAS)
    path('disponibilidad/', DisponibilidadListView.as_view(), name='lista_disponibilidad'),
    path('disponibilidad/crear/', DisponibilidadCreateView.as_view(), name='crear_disponibilidad'),
    path('disponibilidad/<int:pk>/editar/', DisponibilidadUpdateView.as_view(), name='editar_disponibilidad'),
    path('disponibilidad/<int:pk>/eliminar/', DisponibilidadDeleteView.as_view(), name='eliminar_disponibilidad'),
]