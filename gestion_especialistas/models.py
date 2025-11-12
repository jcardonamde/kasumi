# gestion_especialistas/models.py

from django.db import models
from django.conf import settings
from gestion_servicios.models import Servicio # Importamos Servicio para vincular

User = settings.AUTH_USER_MODEL

# ------------------------------------
# 1. Especialista (Vincula Usuario con Especialidad y Servicios)
# ------------------------------------
class Especialista(models.Model):
    # Asumimos que solo los usuarios staff pueden ser especialistas
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, 
                                   limit_choices_to={'is_staff': True}, 
                                   verbose_name='Usuario Especialista')
    
    # Campo para la descripción de su especialidad (e.g., Masajista, Barbero, Estilista)
    especialidad = models.CharField(max_length=150, verbose_name='Especialidad Principal')
    
    # Relación muchos a muchos: ¿Qué servicios puede realizar este especialista?
    servicios = models.ManyToManyField(Servicio, blank=True, related_name='especialistas_aptos', verbose_name='Servicios que realiza')

    is_activo = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = "Especialista"
        verbose_name_plural = "Especialistas"
        ordering = ['usuario__first_name']

    def __str__(self):
        return f"{self.usuario.get_full_name()} ({self.especialidad})"

# ------------------------------------
# 2. Horario Base (Define la jornada laboral)
# ------------------------------------
class HorarioBase(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre del Horario')
    
    # 0=Lunes, 6=Domingo
    DIA_CHOICES = (
        (0, 'Lunes'), (1, 'Martes'), (2, 'Miércoles'), (3, 'Jueves'),
        (4, 'Viernes'), (5, 'Sábado'), (6, 'Domingo'),
    )
    dia_semana = models.IntegerField(choices=DIA_CHOICES, verbose_name='Día de la Semana')
    
    hora_inicio = models.TimeField(verbose_name='Hora de Inicio de Jornada')
    hora_fin = models.TimeField(verbose_name='Hora de Fin de Jornada')

    class Meta:
        verbose_name = "Horario Base"
        verbose_name_plural = "Horarios Base"
        unique_together = ('dia_semana', 'hora_inicio', 'hora_fin')
        ordering = ['dia_semana', 'hora_inicio']

    def __str__(self):
        return f"{self.nombre} ({self.get_dia_semana_display()}: {self.hora_inicio} - {self.hora_fin})"

# ------------------------------------
# 3. Disponibilidad (Asigna Horario a un Especialista)
# ------------------------------------
class Disponibilidad(models.Model):
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE, 
                                     related_name='disponibilidades', 
                                     verbose_name='Especialista')
    
    horario = models.ForeignKey(HorarioBase, on_delete=models.CASCADE, 
                                related_name='especialistas_asignados', 
                                verbose_name='Horario Asignado')
    
    # Si se define una fecha, anula el horario base para ese día.
    fecha_especifica = models.DateField(blank=True, null=True, verbose_name='Fecha Específica (para excepciones)')
    
    class Meta:
        verbose_name = "Disponibilidad del Especialista"
        verbose_name_plural = "Disponibilidades de Especialistas"
        # Restricción: Un especialista solo puede tener una disponibilidad base o una fecha específica asignada una vez
        unique_together = ('especialista', 'horario', 'fecha_especifica')
        ordering = ['especialista__usuario__first_name', 'horario__dia_semana']

    def __str__(self):
        return f"Disp. {self.especialista.usuario.get_full_name()} - {self.horario.nombre}"