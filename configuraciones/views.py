from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ConfiguracionesHomeView(LoginRequiredMixin, TemplateView):
    """
    Vista principal del Módulo de Configuraciones.
    Solo pueden entrar usuarios con un rol que tenga puede_ver_configuracion = True
    o un superusuario.
    """
    template_name = "configuraciones/home_configuraciones.html"

    def dispatch(self, request, *args, **kwargs):
        usuario = request.user

        # Si no está autenticado, que LoginRequiredMixin se encargue
        if not usuario.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        # Obtener los roles asignados al usuario (relación inversa de UsuarioRol)
        roles_asignados = usuario.roles_asignados.select_related('rol')

        # Verificar si alguno de sus roles tiene permiso para ver configuración
        tiene_permiso = any(
            ur.rol.puede_ver_configuracion and ur.rol.esta_activo
            for ur in roles_asignados
        )

        # Si NO tiene permiso y no es superuser → lo mando al home
        if not tiene_permiso and not usuario.is_superuser:
            return redirect('core:home')

        return super().dispatch(request, *args, **kwargs)
