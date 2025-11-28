from django.db import models
from django.conf import settings 

# Opciones para el campo "Tipo de Reporte"
TIPO_REPORTE_CHOICES = (
    ('USUARIOS', 'Usuarios y Roles'),
    ('INGRESOS', 'Ingresos por Periodo'),
    ('FACTURACION', 'Detalle de Facturación'),
    # Puedes añadir más tipos de reportes aquí si es necesario
)

# Opciones para el campo "Estado"
ESTADO_REPORTE_CHOICES = (
    ('PROCESO', 'En proceso'),
    ('COMPLETADO', 'Completado'),
    ('ERROR', 'Error de generación'),
)

class ReporteGenerado(models.Model):
    """Modelo para registrar y auditar un reporte generado en el sistema Kasumi."""
    
    # 1. Tipo de Reporte (Basado en el diagrama)
    tipo_reporte = models.CharField(
        max_length=50, 
        choices=TIPO_REPORTE_CHOICES,
        verbose_name='Tipo de Reporte'
    )
    
    # 2. Fechas de Filtrado (Basado en el diagrama)
    fecha_inicial = models.DateField(
        null=True, blank=True, 
        verbose_name='Fecha Inicial'
    )
    fecha_final = models.DateField(
        null=True, blank=True, 
        verbose_name='Fecha Final'
    )
    
    # 3. Estado (Basado en el diagrama)
    estado = models.CharField(
        max_length=15, 
        choices=ESTADO_REPORTE_CHOICES, 
        default='PROCESO',
        verbose_name='Estado'
    )
    
    # 4. Auditoría
    fecha_generacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Solicitud'
    )
    solicitado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Referencia al modelo de usuario personalizado de Kasumi
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='Solicitado por'
    )

    class Meta:
        verbose_name = "Registro de Reporte"
        verbose_name_plural = "Registro de Reportes"
        # Definición del permiso específico para auditar este modelo
        permissions = [
            ("view_reporte_registro", "Puede ver el registro de reportes generados"),
        ]

    def __str__(self):
        return f"{self.get_tipo_reporte_display()} ({self.get_estado_display()})"
