# gestion_citas/forms.py

from django import forms
from .models import Cita
# Importamos modelos para poder usar QuerySets en los campos.
from django.contrib.auth import get_user_model
from gestion_servicios.models import Servicio 

User = get_user_model()

class CitaForm(forms.ModelForm):
    # Sobrescribimos los campos de ForeignKey para usar QuerySets
    cliente = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True).order_by('first_name'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Cliente'
    )
    
    # Asumimos que los especialistas son usuarios activos que son staff.
    especialista = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True, is_staff=True).order_by('first_name'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Especialista Asignado'
    )
    
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.filter(estado='ACT').order_by('nombre'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Servicio Solicitado'
    )

    class Meta:
        model = Cita
        fields = ['cliente', 'especialista', 'servicio', 'fecha_hora', 'estado']
        widgets = {
            # Usamos un datetime-local widget para una mejor UX
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'fecha_hora': 'Fecha y Hora',
            'estado': 'Estado de la Cita',
        }