# gestion_citas/models.py

from django.db import models
from django.conf import settings

class Cita(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='citas_cliente', verbose_name='Cliente')
    especialista = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='citas_especialista', verbose_name='Especialista')
    
    # Referencia al Servicio del módulo gestion_servicios
    servicio = models.ForeignKey(
        'gestion_servicios.Servicio', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name='Servicio Solicitado'
    )
    
    fecha_hora = models.DateTimeField(verbose_name='Fecha y Hora de la Cita')
    
    ESTADOS_CHOICES = (
        ('PND', 'Pendiente'),
        ('CFM', 'Confirmada'),
        ('CMP', 'Completada'),
        ('CNC', 'Cancelada'),
    )
    estado = models.CharField(max_length=3, choices=ESTADOS_CHOICES, default='PND', verbose_name='Estado de la Cita')
    
    # Auditoría
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='citas_creadas', verbose_name='Creado por')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['fecha_hora']
        # Definición de los permisos granulares para el panel de administración
    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['fecha_hora']
        # Los permisos por defecto se crean automáticamente aquí.

    def __str__(self):
        return f"Cita {self.pk} - {self.cliente.get_full_name()}"