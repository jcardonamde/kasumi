# gestion_clientes/admin.py

from django.contrib import admin
# Importamos el modelo Cliente
from .models import Cliente 


# Usamos el decorador @admin.register para registrar el modelo y la clase de Admin
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # 1. ¿Qué columnas se muestran en la tabla principal de Clientes?
    list_display = (
        'pk', 
        'nombre', 
        'apellido', 
        'email', 
        'telefono', 
        'is_activo', 
        'usuario_registrado'
    )
    
    # 2. Permite buscar por nombre, apellido, email y teléfono (muy útil para atención al cliente)
    search_fields = (
        'nombre', 
        'apellido', 
        'email', 
        'telefono', 
    )
    
    # 3. Permite filtrar la lista de clientes
    list_filter = ('is_activo', 'fecha_creacion')
    
    # 4. Campos que se pueden editar en la interfaz
    fields = ('usuario', 'nombre', 'apellido', 'email', 'telefono', 'is_activo')
    
    # 5. Ordena la lista de clientes por apellido
    ordering = ('apellido',)
    
    # Método para mostrar si el cliente está vinculado a un usuario del sistema (Sí/No)
    def usuario_registrado(self, obj):
        return bool(obj.usuario) # Retorna True si tiene un usuario vinculado
    
    usuario_registrado.short_description = "Usuario Vinculado"
    # Permite filtrar por este campo booleano
    usuario_registrado.boolean = True