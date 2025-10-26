from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    """Administración personalizada de Usuarios en Django Admin."""
    
    # Campos a mostrar en la lista
    list_display = (
        'email', 
        'first_name', 
        'last_name', 
        'numero_documento',
        'is_staff', 
        'is_active',
        'date_joined'
    )
    
    # Filtros laterales
    list_filter = (
        'is_staff', 
        'is_superuser', 
        'is_active', 
        'tipo_documento',
        'date_joined'
    )
    
    # Campos de búsqueda
    search_fields = (
        'email', 
        'first_name', 
        'last_name', 
        'numero_documento',
        'telefono'
    )
    
    # Ordenamiento
    ordering = ('-date_joined',)
    
    # Jerarquía de fechas
    date_hierarchy = 'date_joined'
    
    # Configuración de fieldsets para el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Información Personal'), {
            'fields': (
                'first_name', 
                'last_name', 
                'tipo_documento',
                'numero_documento',
                'fecha_nacimiento'
            )
        }),
        (_('Información de Contacto'), {
            'fields': (
                'telefono',
                'direccion',
                'ciudad'
            )
        }),
        (_('Permisos'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ),
            'classes': ('collapse',)
        }),
        (_('Fechas Importantes'), {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )
    
    # Configuración de fieldsets para agregar usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'tipo_documento',
                'numero_documento',
                'is_staff',
                'is_active'
            ),
        }),
    )
    
    # Campos de solo lectura
    readonly_fields = ('last_login', 'date_joined')
    
    # Configuración de filtros
    filter_horizontal = ('groups', 'user_permissions')
    
    def get_queryset(self, request):
        """Optimiza las consultas."""
        qs = super().get_queryset(request)
        return qs.select_related().prefetch_related('groups', 'user_permissions')
