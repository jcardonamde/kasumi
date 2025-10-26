from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from .models import Rol, UsuarioRol
from accounts.models import Usuario


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
                'placeholder': _('Descripción detallada del rol y sus funciones'),
                'style': 'resize: none;'
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


class UsuarioForm(forms.ModelForm):
    """Formulario para crear/editar usuarios."""
    password1 = forms.CharField(
        label=_('Contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Contraseña')
        }),
        required=False,
        help_text=_('Dejar en blanco si no desea cambiar la contraseña (solo al editar)')
    )
    password2 = forms.CharField(
        label=_('Confirmar Contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Confirmar contraseña')
        }),
        required=False
    )
    
    class Meta:
        model = Usuario
        fields = [
            'tipo_documento', 'numero_documento', 'first_name', 'last_name',
            'telefono', 'direccion', 'ciudad', 'fecha_nacimiento', 'email',
            'is_active', 'is_staff'
        ]
        widgets = {
            'tipo_documento': forms.Select(attrs={
                'class': 'form-select'
            }),
            'numero_documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Número de documento')
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Nombres')
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Apellidos')
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Teléfono')
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': _('Dirección completa'),
                'style': 'resize: none;'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ciudad')
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('correo@ejemplo.com')
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'is_staff': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'tipo_documento': _('Tipo de Documento'),
            'numero_documento': _('Número de Documento'),
            'first_name': _('Nombres'),
            'last_name': _('Apellidos'),
            'telefono': _('Teléfono'),
            'direccion': _('Dirección'),
            'ciudad': _('Ciudad'),
            'fecha_nacimiento': _('Fecha de Nacimiento'),
            'email': _('Correo Electrónico'),
            'is_active': _('Usuario Activo'),
            'is_staff': _('Es Administrador'),
        }
    
    def __init__(self, *args, **kwargs):
        self.is_new = kwargs.pop('is_new', True)
        super().__init__(*args, **kwargs)
        
        # Si es un nuevo usuario, la contraseña es obligatoria
        if self.is_new:
            self.fields['password1'].required = True
            self.fields['password2'].required = True
            self.fields['password1'].help_text = _('Mínimo 8 caracteres')
    
    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')
        # Verificar si ya existe otro usuario con este número de documento
        if self.instance.pk:
            # Estamos editando, excluir el usuario actual
            if Usuario.objects.filter(numero_documento=numero_documento).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(_('Ya existe un usuario con este número de documento.'))
        else:
            # Estamos creando un nuevo usuario
            if Usuario.objects.filter(numero_documento=numero_documento).exists():
                raise forms.ValidationError(_('Ya existe un usuario con este número de documento.'))
        return numero_documento
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verificar si ya existe otro usuario con este email
        if self.instance.pk:
            # Estamos editando, excluir el usuario actual
            if Usuario.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(_('Ya existe un usuario con este correo electrónico.'))
        else:
            # Estamos creando un nuevo usuario
            if Usuario.objects.filter(email=email).exists():
                raise forms.ValidationError(_('Ya existe un usuario con este correo electrónico.'))
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        # Validar que las contraseñas coincidan
        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError(_('Las contraseñas no coinciden.'))
            
            # Validar longitud mínima
            if len(password1) < 8:
                raise forms.ValidationError(_('La contraseña debe tener al menos 8 caracteres.'))
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        
        # Si hay una contraseña, establecerla
        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        return user
