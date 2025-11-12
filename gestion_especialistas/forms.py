# gestion_especialistas/forms.py

from django import forms
from django.contrib.auth import get_user_model
from .models import Especialista, HorarioBase, Disponibilidad

User = get_user_model()

# -----------------
# 1. Formulario para Especialista
# -----------------
class EspecialistaForm(forms.ModelForm):
    # Filtramos el campo 'usuario' para solo mostrar usuarios que son staff (is_staff=True)
    usuario = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=True).exclude(is_superuser=True),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Usuario Asignado'
    )

    class Meta:
        model = Especialista
        fields = ['usuario', 'especialidad', 'servicios', 'is_activo']
        
        widgets = {
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Barbero, Masajista'}),
            # Usamos CheckboxSelectMultiple para la relación ManyToManyField
            'servicios': forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}),
            'is_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'is_activo': 'Especialista Activo'
        }

        # gestion_especialistas/forms.py (AÑADIR AL FINAL)

# ... (El código de EspecialistaForm ya existe arriba) ...

# -----------------
# 2. Formulario para definir Horarios Base
# -----------------
class HorarioBaseForm(forms.ModelForm):
    class Meta:
        model = HorarioBase
        fields = ['nombre', 'dia_semana', 'hora_inicio', 'hora_fin']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Jornada Completa Lunes'}),
            'dia_semana': forms.Select(attrs={'class': 'form-select'}),
            # Usamos TimeInput con type="time" para mejor UX
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
        labels = {
            'dia_semana': 'Día de la Semana',
            'hora_inicio': 'Hora de Inicio',
            'hora_fin': 'Hora de Fin',
        }

        # gestion_especialistas/forms.py (AÑADIR AL FINAL)

# ... (Los formularios EspecialistaForm y HorarioBaseForm ya existen) ...

# -----------------
# 3. Formulario para asignar Disponibilidad a un Especialista
# -----------------
class DisponibilidadForm(forms.ModelForm):
    # Especialista se carga automáticamente al crear la disponibilidad desde el perfil del especialista
    # Aquí lo dejamos como campo regular para el CRUD general
    
    class Meta:
        model = Disponibilidad
        fields = ['especialista', 'horario', 'fecha_especifica']
        
        widgets = {
            'especialista': forms.Select(attrs={'class': 'form-select'}),
            'horario': forms.Select(attrs={'class': 'form-select'}),
            # Usamos DateInput con type="date" para un selector nativo en el navegador
            'fecha_especifica': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'fecha_especifica': 'Fecha Específica (Opcional, para excepciones/días libres)',
        }