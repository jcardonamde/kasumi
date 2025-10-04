"""
WSGI config for kasumi_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kasumi_project.settings')

# Obtiene la aplicación WSGI para este proyecto
application = get_wsgi_application()
