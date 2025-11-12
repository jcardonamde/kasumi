# gestion_agenda/models.py

from django.db import models
from django.conf import settings
from gestion_servicios.models import Servicio # Importamos Servicio para referencia

User = settings.AUTH_USER_MODEL

# Modelo 1: Define un horario genérico (ej: Lunes 9:00 - 18:00)
class Horario(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre del Horario')
    
    # 0=Lunes, 6=Domingo
    DIA_CHOICES = (
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    )
    dia_semana = models.IntegerField(choices=DIA_CHOICES, verbose_name='Día de la Semana')
    
    hora_inicio = models.TimeField(verbose_name='Hora de Inicio de Jornada')
    hora_fin = models.TimeField(verbose_name='Hora de Fin de Jornada')

    class Meta:
        verbose_name = "Horario de Trabajo"
        verbose_name_plural = "Horarios de Trabajo"
        # Restricción: No se puede tener el mismo horario para el mismo día
        unique_together = ('dia_semana', 'hora_inicio', 'hora_fin')
        ordering = ['dia_semana', 'hora_inicio']

    def __str__(self):
        return f"{self.get_dia_semana_display()} de {self.hora_inicio} a {self.hora_fin}"

# Modelo 2: Asigna un Horario a un Especialista
class Disponibilidad(models.Model):
    # Asumimos que el especialista es un usuario con is_staff=True
    especialista = models.ForeignKey(User, on_delete=models.CASCADE, 
                                     related_name='disponibilidades', 
                                     verbose_name='Especialista')
    
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, 
                                related_name='especialistas_disponibles', 
                                verbose_name='Horario Asignado')
    
    # Esto es útil si un especialista tiene un horario diferente en una fecha específica
    fecha_aplicacion = models.DateField(blank=True, null=True, verbose_name='Aplicable desde/Fecha específica')

    class Meta:
        verbose_name = "Disponibilidad del Especialista"
        verbose_name_plural = "Disponibilidades de Especialistas"
        # Restricción: Un especialista solo puede tener un horario definido para una fecha dada (si se usa fecha_aplicacion)
        unique_together = ('especialista', 'horario', 'fecha_aplicacion')

    def __str__(self):
        return f"Disponibilidad de {self.especialista.get_full_name()} - {self.horario}"