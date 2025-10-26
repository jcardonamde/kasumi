from django.contrib import admin
from .models import Rol, UsuarioRol, HistorialUsuario


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    """Administración de Roles en Django Admin."""
    list_display = ('nombre', 'get_estado_display', 'fecha_creacion', 'get_usuarios_count')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'estado')
        }),
        ('Permisos de Usuarios', {
            'fields': (
                'puede_ver_usuarios',
                'puede_crear_usuarios',
                'puede_editar_usuarios',
                'puede_eliminar_usuarios',
            )
        }),
        ('Otros Permisos', {
            'fields': (
                'puede_ver_reportes',
                'puede_ver_configuracion',
            )
        }),
        ('Auditoría', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    
    def get_estado_display(self, obj):
        """Retorna el estado del rol."""
        return obj.get_estado_display()
    get_estado_display.short_description = 'Estado'
    
    def get_usuarios_count(self, obj):
        """Retorna el número de usuarios con este rol."""
        return obj.usuarios_asignados.count()
    get_usuarios_count.short_description = 'Usuarios Asignados'


@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    """Administración de Asignación de Roles en Django Admin."""
    list_display = ('usuario', 'rol', 'fecha_asignacion', 'asignado_por')
    list_filter = ('fecha_asignacion', 'rol')
    search_fields = ('usuario__email', 'usuario__first_name', 'usuario__last_name', 'rol__nombre')
    ordering = ('-fecha_asignacion',)
    
    fieldsets = (
        ('Asignación', {
            'fields': ('usuario', 'rol')
        }),
        ('Auditoría', {
            'fields': ('asignado_por', 'fecha_asignacion'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('fecha_asignacion',)
    
    def save_model(self, request, obj, form, change):
        """Guarda el modelo y registra quién lo asignó."""
        if not change:  # Si es nuevo
            obj.asignado_por = request.user
        super().save_model(request, obj, form, change)


@admin.register(HistorialUsuario)
class HistorialUsuarioAdmin(admin.ModelAdmin):
    """Administración del Historial de Usuarios en Django Admin."""
    list_display = ('usuario', 'get_tipo_accion_display', 'fecha_accion', 'ip_address')
    list_filter = ('tipo_accion', 'fecha_accion')
    search_fields = ('usuario__email', 'usuario__first_name', 'usuario__last_name', 'descripcion')
    ordering = ('-fecha_accion',)
    date_hierarchy = 'fecha_accion'
    
    fieldsets = (
        ('Información', {
            'fields': ('usuario', 'tipo_accion', 'descripcion')
        }),
        ('Detalles Técnicos', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
        ('Auditoría', {
            'fields': ('fecha_accion',),
        }),
    )
    
    readonly_fields = ('fecha_accion', 'usuario', 'tipo_accion', 'descripcion', 'ip_address', 'user_agent')
    
    def get_tipo_accion_display(self, obj):
        """Retorna el tipo de acción en formato legible."""
        return obj.get_tipo_accion_display()
    get_tipo_accion_display.short_description = 'Acción'
    
    # Hacer el historial de solo lectura en el admin
    def has_add_permission(self, request):
        """No permitir agregar registros manualmente."""
        return False
    
    def has_change_permission(self, request, obj=None):
        """No permitir editar registros."""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Permitir eliminar solo a superusuarios."""
        return request.user.is_superuser
