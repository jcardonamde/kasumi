from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Autenticación
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    # Perfil
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
    
    # Gestión de usuarios (solo administradores)
    path('usuarios/', views.ListaUsuariosView.as_view(), name='lista_usuarios'),
    path('usuarios/crear/', views.CrearUsuarioView.as_view(), name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.EditarUsuarioView.as_view(), name='editar_usuario'),
    
    # Redirigir la raíz a login
    path('', views.LoginView.as_view(), name='index'),
]
