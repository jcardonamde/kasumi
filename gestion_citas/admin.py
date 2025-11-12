# gestion_citas/admin.py

from django.contrib import admin
# Importamos el único modelo que has definido en models.py
from .models import Cita 


# Usamos el decorador @admin.register para registrar el modelo y la clase de Admin
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    # 1. ¿Qué columnas se muestran en la tabla principal de citas?
    list_display = (
        'pk', 
        'cliente', 
        'especialista', 
        'fecha_hora', 
        'estado', 
        'servicio_solicitado'
    )
    
    # 2. Permite buscar por el nombre del cliente/especialista
    search_fields = (
        'cliente__first_name', 
        'cliente__last_name', 
        'especialista__first_name', 
        'especialista__last_name',
    )
    
    # 3. Permite filtrar la lista de citas (muy útil)
    list_filter = ('estado', 'fecha_hora', 'servicio')
    
    # 4. Campos de solo lectura (para auditoría)
    readonly_fields = ('fecha_creacion',)
    
    # 5. Agrupación de campos en la vista de detalle
    fieldsets = (
        ("Información General", {
            'fields': ('cliente', 'especialista', 'servicio', 'fecha_hora', 'estado'),
        }),
        ("Auditoría", {
            'fields': ('creado_por', 'fecha_creacion'),
            'classes': ('collapse',), # Esto oculta la sección por defecto para mayor limpieza
        }),
    )
    
    # 6. Método para mostrar el nombre del servicio en la lista
    def servicio_solicitado(self, obj):
        return obj.servicio.nombre if obj.servicio else "N/A"
    
    servicio_solicitado.short_description = "Servicio" # Nombre de la columna
    
    # 7. Prellenar el campo 'creado_por' automáticamente al guardar
    def save_model(self, request, obj, form, change):
        if not change:
            # Si es una nueva cita, asigna el usuario que la crea
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)