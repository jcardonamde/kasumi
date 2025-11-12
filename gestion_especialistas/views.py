# gestion_especialistas/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect

# Importación de Modelos
from .models import Especialista, HorarioBase, Disponibilidad 

# Importación de Formularios (¡ESTA ES LA LÍNEA CORREGIDA!)
from .forms import EspecialistaForm, HorarioBaseForm, DisponibilidadForm 


# ------------------------------------
# Vistas y Mixins de Especialista
# ------------------------------------

# Mixin de permisos
class EspecialistaPermissionMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('accounts:login') 
    permission_required = 'gestion_especialistas.view_especialista'

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar especialistas.")
        return super().handle_no_permission()

# Vistas CRUD para el Modelo ESPECIALISTA
class EspecialistaListView(LoginRequiredMixin, EspecialistaPermissionMixin, ListView):
    model = Especialista
    template_name = 'gestion_especialistas/lista_especialistas.html'
    context_object_name = 'especialistas'

class EspecialistaCreateView(LoginRequiredMixin, EspecialistaPermissionMixin, CreateView):
    model = Especialista
    form_class = EspecialistaForm
    template_name = 'gestion_especialistas/crear_especialista.html'
    success_url = reverse_lazy('gestion_especialistas:lista_especialistas')
    permission_required = 'gestion_especialistas.add_especialista'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'✅ Especialista {self.object.usuario.get_full_name()} creado exitosamente.') 
        return response

class EspecialistaUpdateView(LoginRequiredMixin, EspecialistaPermissionMixin, UpdateView):
    model = Especialista
    form_class = EspecialistaForm
    template_name = 'gestion_especialistas/editar_especialista.html'
    context_object_name = 'especialista'
    success_url = reverse_lazy('gestion_especialistas:lista_especialistas')
    permission_required = 'gestion_especialistas.change_especialista'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'📝 Especialista {self.object.usuario.get_full_name()} actualizado correctamente.')
        return response

class EspecialistaDeleteView(LoginRequiredMixin, EspecialistaPermissionMixin, DeleteView):
    model = Especialista
    template_name = 'gestion_especialistas/eliminar_especialista.html'
    context_object_name = 'especialista'
    success_url = reverse_lazy('gestion_especialistas:lista_especialistas')
    permission_required = 'gestion_especialistas.delete_especialista' 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'🗑️ Especialista {self.object.usuario.get_full_name()} eliminado exitosamente.')
        return response


# ------------------------------------
# Vistas y Mixins de Horario Base
# ------------------------------------

# Mixin de permisos para Horarios Base
class HorarioBasePermissionMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('accounts:login') 
    permission_required = 'gestion_especialistas.view_horariobase'

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar horarios base.")
        return super().handle_no_permission()

# Vistas CRUD para el Modelo HORARIOBASE
class HorarioBaseListView(LoginRequiredMixin, HorarioBasePermissionMixin, ListView):
    model = HorarioBase
    template_name = 'gestion_especialistas/lista_horarios.html'
    context_object_name = 'horarios'

class HorarioBaseCreateView(LoginRequiredMixin, HorarioBasePermissionMixin, CreateView):
    model = HorarioBase
    form_class = HorarioBaseForm
    template_name = 'gestion_especialistas/crear_horario.html'
    success_url = reverse_lazy('gestion_especialistas:lista_horarios')
    permission_required = 'gestion_especialistas.add_horariobase'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '✅ Horario Base creado exitosamente.') 
        return response

class HorarioBaseUpdateView(LoginRequiredMixin, HorarioBasePermissionMixin, UpdateView):
    model = HorarioBase
    form_class = HorarioBaseForm
    template_name = 'gestion_especialistas/editar_horario.html'
    success_url = reverse_lazy('gestion_especialistas:lista_horarios')
    permission_required = 'gestion_especialistas.change_horariobase'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '📝 Horario Base actualizado correctamente.')
        return response

class HorarioBaseDeleteView(LoginRequiredMixin, HorarioBasePermissionMixin, DeleteView):
    model = HorarioBase
    template_name = 'gestion_especialistas/eliminar_horario.html'
    context_object_name = 'horario'
    success_url = reverse_lazy('gestion_especialistas:lista_horarios')
    permission_required = 'gestion_especialistas.delete_horariobase' 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '🗑️ Horario Base eliminado exitosamente.')
        return response


# ------------------------------------
# Vistas y Mixins de Disponibilidad
# ------------------------------------

# Mixin de permisos para Disponibilidad
class DisponibilidadPermissionMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('accounts:login') 
    permission_required = 'gestion_especialistas.view_disponibilidad'

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar la disponibilidad.")
        return super().handle_no_permission()

# Vistas CRUD para el Modelo DISPONIBILIDAD
class DisponibilidadListView(LoginRequiredMixin, DisponibilidadPermissionMixin, ListView):
    model = Disponibilidad
    template_name = 'gestion_especialistas/disponibilidad/lista_disponibilidad.html'
    context_object_name = 'disponibilidades'

class DisponibilidadCreateView(LoginRequiredMixin, DisponibilidadPermissionMixin, CreateView):
    model = Disponibilidad
    form_class = DisponibilidadForm
    template_name = 'gestion_especialistas/disponibilidad/crear_disponibilidad.html'
    success_url = reverse_lazy('gestion_especialistas:lista_disponibilidad')
    permission_required = 'gestion_especialistas.add_disponibilidad'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '✅ Disponibilidad asignada exitosamente.') 
        return response

class DisponibilidadUpdateView(LoginRequiredMixin, DisponibilidadPermissionMixin, UpdateView):
    model = Disponibilidad
    form_class = DisponibilidadForm
    template_name = 'gestion_especialistas/disponibilidad/editar_disponibilidad.html'
    success_url = reverse_lazy('gestion_especialistas:lista_disponibilidad')
    permission_required = 'gestion_especialistas.change_disponibilidad'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '📝 Disponibilidad actualizada correctamente.')
        return response

class DisponibilidadDeleteView(LoginRequiredMixin, DisponibilidadPermissionMixin, DeleteView):
    model = Disponibilidad
    template_name = 'gestion_especialistas/disponibilidad/eliminar_disponibilidad.html'
    context_object_name = 'disponibilidad'
    success_url = reverse_lazy('gestion_especialistas:lista_disponibilidad')
    permission_required = 'gestion_especialistas.delete_disponibilidad' 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '🗑️ Disponibilidad eliminada exitosamente.')
        return response