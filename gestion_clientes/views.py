# gestion_clientes/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm

# Mixin de permisos
class ClientePermissionMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('accounts:login') 
    permission_required = 'gestion_clientes.view_cliente'

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar clientes.")
        return super().handle_no_permission()

# ------------------------------------
# Vistas CRUD para el Modelo CLIENTE
# ------------------------------------

class ClienteListView(LoginRequiredMixin, ClientePermissionMixin, ListView):
    model = Cliente
    template_name = 'gestion_clientes/lista_clientes.html'
    context_object_name = 'clientes'

class ClienteCreateView(LoginRequiredMixin, ClientePermissionMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion_clientes/crear_cliente.html'
    success_url = reverse_lazy('gestion_clientes:lista_clientes')
    permission_required = 'gestion_clientes.add_cliente'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'✅ Cliente "{self.object.get_full_name()}" creado exitosamente.') 
        return response

class ClienteUpdateView(LoginRequiredMixin, ClientePermissionMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'gestion_clientes/editar_cliente.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('gestion_clientes:lista_clientes')
    permission_required = 'gestion_clientes.change_cliente'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'📝 Cliente "{self.object.get_full_name()}" actualizado correctamente.')
        return response

class ClienteDeleteView(LoginRequiredMixin, ClientePermissionMixin, DeleteView):
    model = Cliente
    template_name = 'gestion_clientes/eliminar_cliente.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('gestion_clientes:lista_clientes')
    permission_required = 'gestion_clientes.delete_cliente' 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'🗑️ Cliente "{self.object.get_full_name()}" eliminado exitosamente.')
        return response