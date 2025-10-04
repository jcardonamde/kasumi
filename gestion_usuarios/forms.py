from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from .models import Rol, UsuarioRol


class RolForm(forms.ModelForm):
    """Formulario para crear/editar roles."""
    class Meta:
        model = Rol
        fields = [
            'nombre', 'descripcion', 'estado',
            'puede_ver_usuarios', 'puede_crear_usuarios',
            'puede_editar_usuarios', 'puede_eliminar_usuarios',
            'puede_ver_reportes', 'puede_ver_configuracion'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ej: Administrador, Recepcionista, etc.')
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': _('Descripción detallada del rol y sus funciones')
            }),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadir clases a los campos de checkbox
        for field in self.fields:
            if isinstance(self.fields[field], forms.BooleanField):
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})


class AsignarRolForm(forms.ModelForm):
    """Formulario para asignar roles a usuarios."""
    class Meta:
        model = UsuarioRol
        fields = ['rol']
        widgets = {
            'rol': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo roles activos
        self.fields['rol'].queryset = Rol.objects.filter(estado='A')


class CambiarContrasenaForm(PasswordChangeForm):
    """Formulario para cambiar la contraseña."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar los campos
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Contraseña actual')
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Nueva contraseña')
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Confirmar nueva contraseña')
        })


class RestablecerContrasenaForm(SetPasswordForm):
    """Formulario para restablecer la contraseña."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar los campos
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Nueva contraseña')
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Confirmar nueva contraseña')
        })
