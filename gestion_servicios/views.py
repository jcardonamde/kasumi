# gestion_servicios/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Servicio
from .forms import ServicioForm

class ServicioPermissionMixin(PermissionRequiredMixin):
    # Debe ser configurado en el Admin con permisos como 'gestion_servicios.view_servicio'
    login_url = reverse_lazy('accounts:login') 
    
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar servicios.")
        return super().handle_no_permission()

# Vista de Listado (Read)
class ServicioListView(LoginRequiredMixin, ServicioPermissionMixin, ListView):
    model = Servicio
    template_name = 'gestion_servicios/lista_servicios.html'
    context_object_name = 'servicios'
    permission_required = 'gestion_servicios.view_servicio' 
    
# Vista de Creación (Create)
class ServicioCreateView(LoginRequiredMixin, ServicioPermissionMixin, CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'gestion_servicios/crear_servicio.html'
    success_url = reverse_lazy('gestion_servicios:lista_servicios')
    permission_required = 'gestion_servicios.add_servicio'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '✨ Servicio creado exitosamente.') 
        return response

# Vista de Actualización (Update)
class ServicioUpdateView(LoginRequiredMixin, ServicioPermissionMixin, UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'gestion_servicios/editar_servicio.html'
    success_url = reverse_lazy('gestion_servicios:lista_servicios')
    permission_required = 'gestion_servicios.change_servicio'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '📝 Servicio actualizado correctamente.')
        return response

# Vista de Eliminación (Delete)
class ServicioDeleteView(LoginRequiredMixin, ServicioPermissionMixin, DeleteView):
    model = Servicio
    template_name = 'gestion_servicios/eliminar_servicio.html'
    context_object_name = 'servicio'
    success_url = reverse_lazy('gestion_servicios:lista_servicios')
    permission_required = 'gestion_servicios.delete_servicio' 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '🗑️ Servicio eliminado exitosamente.')
        return response