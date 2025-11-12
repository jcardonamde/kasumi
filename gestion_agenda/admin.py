# gestion_agenda/admin.py

from django.contrib import admin
# ¡IMPORTACIÓN CORREGIDA!
# Importamos los nombres correctos: Horario y Disponibilidad
from .models import Horario, Disponibilidad 


# 1. Registra el modelo Horario
@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista de la administración
    list_display = ('nombre', 'get_dia_semana_display', 'hora_inicio', 'hora_fin')
    # Permite filtrar por día de la semana
    list_filter = ('dia_semana',)
    # Permite buscar por nombre
    search_fields = ('nombre',)
    
    
# 2. Registra el modelo Disponibilidad
@admin.register(Disponibilidad)
class DisponibilidadAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista de la administración
    list_display = ('especialista', 'horario', 'fecha_aplicacion')
    # Permite filtrar por especialista y horario
    list_filter = ('especialista', 'horario')
    # Permite buscar por el nombre del especialista
    search_fields = ('especialista__username', 'especialista__first_name', 'especialista__last_name')
    # Mejora la interfaz de selección para los campos de relación
    raw_id_fields = ('especialista', 'horario')