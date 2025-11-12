# gestion_agenda/urls.py

from django.urls import path
from . import views 
from .views import (
    AgendaIndexView,
    HorarioListView, HorarioCreateView, HorarioUpdateView, HorarioDeleteView
)

app_name = 'gestion_agenda'

urlpatterns = [
    # Vista principal de la Agenda (Calendario)
    path('', AgendaIndexView.as_view(), name='index_agenda'),
    
    # CRUD de Horarios de Trabajo
    path('horarios/', HorarioListView.as_view(), name='lista_horarios'),
    path('horarios/crear/', HorarioCreateView.as_view(), name='crear_horario'),
    path('horarios/<int:pk>/editar/', HorarioUpdateView.as_view(), name='editar_horario'),
    path('horarios/<int:pk>/eliminar/', HorarioDeleteView.as_view(), name='eliminar_horario'),
    
    # CRUD de Disponibilidad se añadirá después
]