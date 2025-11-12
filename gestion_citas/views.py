# gestion_citas/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Cita
from .forms import CitaForm

class CitaPermissionMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('accounts:login') 
    
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar citas.")
        return super().handle_no_permission()

# Vista de Listado (Read)
class CitaListView(LoginRequiredMixin, CitaPermissionMixin, ListView):
    model = Cita
    # Nomenclatura en subcarpeta 'citas' para evitar colisiones
    template_name = 'gestion_citas/lista_citas.html' 
    context_object_name = 'citas'
    permission_required = 'gestion_citas.view_cita' 
    
# Vista de Creación (Create)
class CitaCreateView(LoginRequiredMixin, CitaPermissionMixin, CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'gestion_citas/crear_cita.html'
    success_url = reverse_lazy('gestion_citas:lista_citas')
    permission_required = 'gestion_citas.add_cita'

    def form_valid(self, form):
        # Asigna el usuario actual como el creador de la cita
        form.instance.creado_por = self.request.user 
        response = super().form_valid(form)
        messages.success(self.request, '✅ Cita creada exitosamente.') 
        return response

# Vista de Actualización (Update)
class CitaUpdateView(LoginRequiredMixin, CitaPermissionMixin, UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'gestion_citas/editar_cita.html'
    success_url = reverse_lazy('gestion_citas:lista_citas')
    permission_required = 'gestion_citas.change_cita'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '📝 Cita actualizada correctamente.')
        return response

# Vista de Eliminación (Delete)
class CitaDeleteView(LoginRequiredMixin, CitaPermissionMixin, DeleteView):
    model = Cita
    template_name = 'gestion_citas/eliminar_cita.html'
    context_object_name = 'cita'
    success_url = reverse_lazy('gestion_citas:lista_citas')
    permission_required = 'gestion_citas.delete_cita' 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '🗑️ Cita eliminada exitosamente.')
        return response