# gestion_especialistas/admin.py

from django.contrib import admin
# Importamos los tres modelos que has definido
from .models import Especialista, HorarioBase, Disponibilidad 


# --- CONFIGURACIÓN PARA EL MODELO 1: ESPECIALISTA ---

@admin.register(Especialista)
class EspecialistaAdmin(admin.ModelAdmin):
    # Columnas que se muestran en la lista
    list_display = (
        'usuario_nombre_completo', 
        'especialidad', 
        'is_activo', 
        'mostrar_servicios'
    )
    
    # Filtros laterales
    list_filter = ('is_activo', 'especialidad', 'servicios')
    
    # Campos de búsqueda
    search_fields = (
        'usuario__first_name', 
        'usuario__last_name', 
        'especialidad'
    )
    
    # Muestra los campos en el formulario, agrupados
    fieldsets = (
        ("Información Básica", {
            'fields': ('usuario', 'especialidad', 'is_activo'),
        }),
        ("Servicios Aptos", {
            'fields': ('servicios',),
        }),
    )
    
    # Ordenar por el nombre del usuario
    ordering = ('usuario__first_name',)

    # Método para mostrar el nombre completo del usuario
    def usuario_nombre_completo(self, obj):
        return obj.usuario.get_full_name()
    usuario_nombre_completo.short_description = 'Nombre del Especialista'

    # Método para mostrar los servicios como texto en la lista
    def mostrar_servicios(self, obj):
        return ", ".join([s.nombre for s in obj.servicios.all()])
    mostrar_servicios.short_description = 'Servicios Realizados'


# --- CONFIGURACIÓN PARA EL MODELO 2: HORARIOBASE ---

@admin.register(HorarioBase)
class HorarioBaseAdmin(admin.ModelAdmin):
    # Columnas que se muestran en la lista
    list_display = (
        'nombre', 
        'get_dia_semana_display', 
        'hora_inicio', 
        'hora_fin'
    )
    
    # Filtros laterales
    list_filter = ('dia_semana',)
    
    # Campos de búsqueda
    search_fields = ('nombre',)
    
    # Ordenar por el día de la semana
    ordering = ('dia_semana', 'hora_inicio')


# --- CONFIGURACIÓN PARA EL MODELO 3: DISPONIBILIDAD ---

@admin.register(Disponibilidad)
class DisponibilidadAdmin(admin.ModelAdmin):
    # Columnas que se muestran en la lista
    list_display = (
        'especialista', 
        'horario', 
        'fecha_especifica', 
        'es_excepcion'
    )
    
    # Filtros laterales
    list_filter = ('horario', 'fecha_especifica')
    
    # Campos de búsqueda
    search_fields = (
        'especialista__usuario__first_name', 
        'horario__nombre'
    )
    
    # Método para determinar si es una excepción (si tiene fecha específica)
    def es_excepcion(self, obj):
        return bool(obj.fecha_especifica)
    es_excepcion.short_description = 'Excepción de Fecha'
    es_excepcion.boolean = True