# gestion_agenda/forms.py

from django import forms
from django.contrib.auth import get_user_model
from .models import Horario, Disponibilidad

User = get_user_model()

# -----------------
# 1. Formulario para definir Horarios de Trabajo
# -----------------
class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['nombre', 'dia_semana', 'hora_inicio', 'hora_fin']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dia_semana': forms.Select(attrs={'class': 'form-select'}),
            # Usamos TimeInput con type="time" para mejor UX en navegadores
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
        labels = {
            'dia_semana': 'Día de la Semana',
            'hora_inicio': 'Hora de Inicio',
            'hora_fin': 'Hora de Fin',
        }

# -----------------
# 2. Formulario para asignar Disponibilidad a un Especialista
# -----------------
class DisponibilidadForm(forms.ModelForm):
    # Sobrescribimos el campo especialista para filtrar solo usuarios staff (posibles especialistas)
    especialista = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=True).order_by('first_name'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Especialista'
    )

    class Meta:
        model = Disponibilidad
        fields = ['especialista', 'horario', 'fecha_aplicacion']
        
        widgets = {
            'horario': forms.Select(attrs={'class': 'form-select'}),
            # Usamos DateInput con type="date"
            'fecha_aplicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'fecha_aplicacion': 'Fecha de Aplicación (Opcional)',
        }