# gestion_clientes/urls.py

from django.urls import path
from .views import (
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
)

app_name = 'gestion_clientes'

urlpatterns = [
    # CRUD de Clientes
    path('', ClienteListView.as_view(), name='lista_clientes'),
    path('crear/', ClienteCreateView.as_view(), name='crear_cliente'),
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='eliminar_cliente'),
]