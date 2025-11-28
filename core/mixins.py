# core/mixins.py

from django.contrib.auth.mixins import UserPassesTestMixin

class PermisoReportesMixin(UserPassesTestMixin):
    def test_func(self):
        # Esta es la lógica de permisos. Se asume que solo el staff puede ver reportes.
        if self.request.user.is_authenticated:
            return self.request.user.is_staff or self.request.user.is_superuser
        return False