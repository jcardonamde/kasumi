from django.db import models
from django.utils.translation import gettext_lazy as _


class Rol(models.Model):
    """Modelo para los roles de usuario en el sistema."""
    
    class Estado(models.TextChoices):
        ACTIVO = 'A', _('Activo')
        INACTIVO = 'I', _('Inactivo')
    
    nombre = models.CharField(max_length=50, unique=True, verbose_name=_('Nombre del Rol'))
    descripcion = models.TextField(blank=True, verbose_name=_('Descripción'))
    estado = models.CharField(
        max_length=1,
        choices=Estado.choices,
        default=Estado.ACTIVO,
        verbose_name=_('Estado')
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de Creación'))
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name=_('Última Actualización'))
    
    # Permisos específicos para este rol
    puede_ver_usuarios = models.BooleanField(default=False, verbose_name=_('Puede ver usuarios'))
    puede_crear_usuarios = models.BooleanField(default=False, verbose_name=_('Puede crear usuarios'))
    puede_editar_usuarios = models.BooleanField(default=False, verbose_name=_('Puede editar usuarios'))
    puede_eliminar_usuarios = models.BooleanField(default=False, verbose_name=_('Puede eliminar usuarios'))
    
    # Otros permisos que podrías necesitar
    puede_ver_reportes = models.BooleanField(default=False, verbose_name=_('Puede ver reportes'))
    puede_ver_configuracion = models.BooleanField(default=False, verbose_name=_('Puede ver configuración'))
    
    class Meta:
        verbose_name = _('Rol')
        verbose_name_plural = _('Roles')
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
    @property
    def esta_activo(self):
        return self.estado == self.Estado.ACTIVO


class UsuarioRol(models.Model):
    """Modelo intermedio para la relación muchos a muchos entre Usuario y Rol."""
    from accounts.models import Usuario  # Importación local para evitar importación circular
    
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='roles_asignados',
        verbose_name=_('Usuario')
    )
    rol = models.ForeignKey(
        Rol,
        on_delete=models.CASCADE,
        related_name='usuarios_asignados',
        verbose_name=_('Rol')
    )
    fecha_asignacion = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de Asignación'))
    asignado_por = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='roles_asignados_por_mi',
        verbose_name=_('Asignado por')
    )
    
    class Meta:
        verbose_name = _('Asignación de Rol')
        verbose_name_plural = _('Asignaciones de Roles')
        unique_together = ('usuario', 'rol')
    
    def __str__(self):
        return f"{self.usuario} - {self.rol}"


class HistorialUsuario(models.Model):
    """Modelo para registrar el historial de acciones de los usuarios."""
    
    class TipoAccion(models.TextChoices):
        LOGIN = 'login', _('Inicio de sesión')
        LOGOUT = 'logout', _('Cierre de sesión')
        CREACION = 'creacion', _('Creación de registro')
        ACTUALIZACION = 'actualizacion', _('Actualización de registro')
        ELIMINACION = 'eliminacion', _('Eliminación de registro')
        CAMBIO_CONTRASENA = 'cambio_contrasena', _('Cambio de contraseña')
    
    from accounts.models import Usuario  # Importación local para evitar importación circular
    
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='historial',
        verbose_name=_('Usuario')
    )
    fecha_accion = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de la Acción'))
    tipo_accion = models.CharField(
        max_length=20,
        choices=TipoAccion.choices,
        verbose_name=_('Tipo de Acción')
    )
    descripcion = models.TextField(verbose_name=_('Descripción'))
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('Dirección IP'))
    user_agent = models.TextField(blank=True, null=True, verbose_name=_('User Agent'))
    
    class Meta:
        verbose_name = _('Entrada de Historial')
        verbose_name_plural = _('Historial de Usuarios')
        ordering = ['-fecha_accion']
    
    def __str__(self):
        return f"{self.usuario} - {self.get_tipo_accion_display()} - {self.fecha_accion}"
