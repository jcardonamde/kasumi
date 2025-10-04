from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'gestion_usuarios'

urlpatterns = [
    # Rutas para la gestión de roles
    path('roles/', 
         login_required(views.ListaRolesView.as_view()), 
         name='lista_roles'),
    path('roles/crear/', 
         login_required(views.CrearRolView.as_view()), 
         name='crear_rol'),
    path('roles/editar/<int:pk>/', 
         login_required(views.EditarRolView.as_view()), 
         name='editar_rol'),
    path('roles/eliminar/<int:pk>/', 
         login_required(views.EliminarRolView.as_view()), 
         name='eliminar_rol'),
    
    # Rutas para la gestión de usuarios
    path('usuarios/', 
         login_required(views.ListaUsuariosView.as_view()), 
         name='lista_usuarios'),
    path('usuarios/<int:pk>/', 
         login_required(views.DetalleUsuarioView.as_view()), 
         name='detalle_usuario'),
    path('usuarios/<int:pk>/cambiar-contrasena/', 
         login_required(views.CambiarContrasenaView.as_view()), 
         name='cambiar_contrasena'),
    
    # Rutas para la asignación de roles
    path('usuarios/<int:usuario_id>/asignar-rol/', 
         login_required(views.AsignarRolView.as_view()), 
         name='asignar_rol'),
    path('usuarios/rol/<int:pk>/quitar/', 
         login_required(views.QuitarRolView.as_view()), 
         name='quitar_rol'),
]
