from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Usuario

class LoginForm(AuthenticationForm):
    """Formulario de inicio de sesión personalizado."""
    username = forms.EmailField(
        label=_("Correo Electrónico"),
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': _('correo@ejemplo.com'),
            'autofocus': True
        })
    )
    password = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Contraseña')
        }),
    )
    
    error_messages = {
        'invalid_login': _(
            "Por favor ingrese un correo y contraseña correctos. "
            "Note que ambos campos pueden ser sensibles a mayúsculas y minúsculas."
        ),
        'inactive': _("Esta cuenta está inactiva."),
    }


class UsuarioForm(forms.ModelForm):
    """Formulario para crear/editar usuarios."""
    password1 = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        required=False,
        help_text=_("Ingrese una contraseña segura.")
    )
    password2 = forms.CharField(
        label=_("Confirmar Contraseña"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        required=False,
        help_text=_("Ingrese la misma contraseña para verificación.")
    )
    
    class Meta:
        model = Usuario
        fields = [
            'email', 'first_name', 'last_name', 'tipo_documento', 
            'numero_documento', 'telefono', 'direccion', 'ciudad', 
            'fecha_nacimiento', 'is_active', 'is_staff'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        # Solo validar contraseñas si se están actualizando
        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', _("Las contraseñas no coinciden."))
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Actualizar contraseña si se proporcionó
        password = self.cleaned_data.get("password1")
        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        
        return user
