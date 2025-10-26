#!/usr/bin/env python
"""
Script para crear un usuario administrador de prueba
Ejecutar con: python crear_usuario_admin.py
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kasumi_project.settings')
django.setup()

from accounts.models import Usuario

def crear_admin():
    """Crea un usuario administrador si no existe"""
    email = 'admin@kasumi.com'
    
    # Verificar si ya existe
    if Usuario.objects.filter(email=email).exists():
        print(f"✅ El usuario {email} ya existe")
        usuario = Usuario.objects.get(email=email)
        print(f"   Nombre: {usuario.get_full_name()}")
        print(f"   Es administrador: {usuario.is_staff}")
        return
    
    # Crear el usuario
    usuario = Usuario.objects.create_user(
        email=email,
        password='admin123',
        first_name='Administrador',
        last_name='Kasumi',
        tipo_documento='CC',
        numero_documento='1234567890',
        telefono='3001234567',
        direccion='Calle 123 #45-67',
        ciudad='Bogotá',
        is_staff=True,
        is_superuser=True,
        is_active=True
    )
    
    print("✅ Usuario administrador creado exitosamente!")
    print(f"   Email: {email}")
    print(f"   Contraseña: admin123")
    print(f"   Nombre: {usuario.get_full_name()}")
    print("\n⚠️  IMPORTANTE: Cambia la contraseña después del primer login")

if __name__ == '__main__':
    crear_admin()
