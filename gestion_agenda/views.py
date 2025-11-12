# gestion_agenda/views.py

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AgendaIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'gestion_agenda/index_agenda.html'
    # TODO: Aquí se implementará la lógica de calendario

    # gestion_agenda/views.py (AÑADIR AL FINAL)

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Horario, Disponibilidad
from .forms import HorarioForm, DisponibilidadForm

# Mixin de permisos para Horarios
class HorarioPermissionMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('accounts:login') 
    permission_required = 'gestion_agenda.view_horario' # Necesitas crear este permiso en admin si no existe

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar horarios.")
        return super().handle_no_permission()

# ------------------------------------
# Vistas CRUD para el Modelo HORARIO
# ------------------------------------

class HorarioListView(LoginRequiredMixin, HorarioPermissionMixin, ListView):
    model = Horario
    template_name = 'gestion_agenda/lista_horarios.html'
    context_object_name = 'horarios'
    # Nota: Los permisos se crean automáticamente (add_horario, change_horario, delete_horario, view_horario)

class HorarioCreateView(LoginRequiredMixin, HorarioPermissionMixin, CreateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'gestion_agenda/crear_horario.html'
    success_url = reverse_lazy('gestion_agenda:lista_horarios')
    permission_required = 'gestion_agenda.add_horario'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '✅ Horario creado exitosamente.') 
        return response

class HorarioUpdateView(LoginRequiredMixin, HorarioPermissionMixin, UpdateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'gestion_agenda/editar_horario.html'
    success_url = reverse_lazy('gestion_agenda:lista_horarios')
    permission_required = 'gestion_agenda.change_horario'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '📝 Horario actualizado correctamente.')
        return response

class HorarioDeleteView(LoginRequiredMixin, HorarioPermissionMixin, DeleteView):
    model = Horario
    template_name = 'gestion_agenda/eliminar_horario.html'
    context_object_name = 'horario'
    success_url = reverse_lazy('gestion_agenda:lista_horarios')
    permission_required = 'gestion_agenda.delete_horario' 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '🗑️ Horario eliminado exitosamente.')
        return response