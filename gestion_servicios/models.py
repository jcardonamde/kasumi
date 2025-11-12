# gestion_servicios/models.py

from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre del Servicio')
    descripcion = models.TextField(blank=True, verbose_name='Descripción Detallada')
    duracion_minutos = models.IntegerField(default=60, verbose_name='Duración (minutos)')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Base')
    
    ACTIVO_CHOICES = (
        ('ACT', 'Activo'),
        ('INA', 'Inactivo'),
    )
    estado = models.CharField(max_length=3, choices=ACTIVO_CHOICES, default='ACT', verbose_name='Estado')

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} (${self.precio})"