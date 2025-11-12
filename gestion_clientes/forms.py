# gestion_clientes/forms.py

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'is_activo', 'usuario']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: +57 300 123 4567'}),
            'is_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'usuario': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'is_activo': 'Cliente Activo',
        }
    
    # Método para asegurar que el campo usuario sea opcional y no dé errores en la interfaz
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacemos que el campo de usuario sea opcional en el formulario HTML
        self.fields['usuario'].required = False
        # Permite seleccionar un valor vacío (None)
        self.fields['usuario'].empty_label = "No asignar a usuario del sistema"