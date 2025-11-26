# gestion_especialistas/forms.py

from django import forms
from django.contrib.auth import get_user_model
from .models import Especialista, HorarioBase, Disponibilidad 

User = get_user_model()

# -----------------
# 1. Formulario para Especialista
# -----------------
class EspecialistaForm(forms.ModelForm):
    # Definición más robusta para el campo obligatorio 'usuario'.
    # Filtra: Solo usuarios que son staff (is_staff=True). Incluimos superusuarios por si acaso.
    usuario = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=True).order_by('first_name'),
        # Nota: He ELIMINADO el .exclude(is_superuser=True) para que al menos el Admin aparezca
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Usuario Asignado (Debe ser staff)'
    )

    class Meta:
        model = Especialista
        fields = ['usuario', 'especialidad', 'servicios', 'is_activo']
        
        widgets = {
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Barbero, Masajista'}),
            'servicios': forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}),
            'is_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'is_activo': 'Especialista Activo'
        }


# -----------------
# 2. Formulario para HorarioBase
# -----------------
class HorarioBaseForm(forms.ModelForm):
    class Meta:
        model = HorarioBase
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Jornada Completa'}),
            'dia_semana': forms.Select(attrs={'class': 'form-select'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
        labels = {
            'dia_semana': 'Día de la Semana',
            'hora_inicio': 'Hora de Inicio',
            'hora_fin': 'Hora de Fin',
        }


# -----------------
# 3. Formulario para asignar Disponibilidad a un Especialista
# -----------------
class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['especialista', 'horario', 'fecha_especifica']
        
        widgets = {
            'especialista': forms.Select(attrs={'class': 'form-select'}),
            'horario': forms.Select(attrs={'class': 'form-select'}),
            'fecha_especifica': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }