from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Página de inicio - redirige al login si no está autenticado
    path('', views.HomeView.as_view(), name='home'),
    
    # Dashboard principal
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    
    # Otras páginas estáticas pueden ir aquí
]
