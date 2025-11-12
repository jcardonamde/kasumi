# gestion_servicios/forms.py

from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'duracion_minutos', 'precio', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracion_minutos': forms.NumberInput(attrs={'class': 'form-control', 'min': 10}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }