# reportes/admin.py

from django.contrib import admin
from .models import ReporteGenerado 

@admin.register(ReporteGenerado)
class ReporteGeneradoAdmin(admin.ModelAdmin):
    """Configuración de cómo se ve el modelo ReporteGenerado en el Admin."""
    
    # Campos que se muestran en la lista de registros
    list_display = ('id', 'tipo_reporte', 'fecha_generacion', 'estado', 'solicitado_por', 'fecha_inicial', 'fecha_final',)
    list_filter = ('estado', 'tipo_reporte', 'fecha_generacion',)
    search_fields = ('tipo_reporte',)