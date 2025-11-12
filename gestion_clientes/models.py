# gestion_clientes/models.py

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Cliente(models.Model):
    """
    Representa un cliente que utiliza los servicios. 
    Puede estar vinculado a un usuario del sistema (opcional).
    """
    # Vinculación opcional a un usuario del sistema (si se registra con login)
    usuario = models.OneToOneField(User, 
                                   on_delete=models.SET_NULL, 
                                   null=True, blank=True, 
                                   related_name='perfil_cliente', 
                                   verbose_name='Usuario del Sistema')
    
    # Información básica del cliente (puede ser usada aunque 'usuario' sea NULL)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')
    
    # Campo de gestión
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    is_activo = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_full_name(self):
        """Retorna el nombre completo del cliente."""
        return f"{self.nombre} {self.apellido}"