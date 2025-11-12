# gestion_servicios/admin.py

from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion_minutos', 'precio', 'estado')
    list_filter = ('estado', 'duracion_minutos')
    search_fields = ('nombre', 'descripcion')