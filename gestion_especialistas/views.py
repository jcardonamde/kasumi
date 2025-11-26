# gestion_especialistas/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin # <--- ¡IMPORTACIÓN CORREGIDA!
from django.contrib import messages
from django.shortcuts import render, redirect

# Importación de Modelos
from .models import Especialista, HorarioBase, Disponibilidad 

# Importación de Formularios
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

    # Lógica para guardar correctamente los campos Many-to-Many
    def form_valid(self, form):
        # 1. Guardar el objeto sin commit (necesario para campos M2M/O2O)
        self.object = form.save(commit=False)
        
        # 2. Guardamos el objeto base en la DB
        self.object.save()
        
        # 3. Guardamos las relaciones Many-to-Many (Servicios)
        form.save_m2m()
        
        messages.success(self.request, f'✅ Especialista {self.object.usuario.get_full_name()} creado exitosamente.') 
        
        return redirect(self.get_success_url())

    # Lógica para mostrar los errores de validación
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"⚠️ Error en {field}: {error}")
        return super().form_invalid(form)


class EspecialistaUpdateView(LoginRequiredMixin, EspecialistaPermissionMixin, UpdateView):
    model = Especialista
    form_class = EspecialistaForm
    template_name = 'gestion_especialistas/editar_especialista.html'
    context_object_name = 'especialista'
    success_url = reverse_lazy('gestion_especialistas:lista_especialistas')
    permission_required = 'gestion_especialistas.change_especialista'

    # Lógica para guardar correctamente los campos Many-to-Many
    def form_valid(self, form):
        # 1. Guardar el objeto sin commit
        self.object = form.save(commit=False)
        
        # 2. Guardamos el objeto base
        self.object.save()
        
        # 3. Guardamos las relaciones Many-to-Many ('servicios').
        form.save_m2m()

        messages.success(self.request, f'📝 Especialista {self.object.usuario.get_full_name()} actualizado correctamente.')
        
        return redirect(self.get_success_url())

    # Lógica para mostrar los errores de validación
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"⚠️ Error en {field}: {error}")
        return super().form_invalid(form)


class EspecialistaDeleteView(LoginRequiredMixin, EspecialistaPermissionMixin, DeleteView):
    model = Especialista
    template_name = 'gestion_especialistas/eliminar_especialista.html'
    context_object_name = 'especialista'
    success_url = reverse_lazy('gestion_especialistas:lista_especialistas')
    permission_required = 'gestion_especialistas.delete_especialista'

    def form_valid(self, form):
        messages.success(self.request, f'🗑️ Especialista {self.object.usuario.get_full_name()} eliminado exitosamente.') 
        return super().form_valid(form)


# ------------------------------------
# Vistas CRUD para el Modelo HorarioBase
# ------------------------------------

# ... (El resto de las vistas CRUD para HorarioBase y Disponibilidad sigue aquí)

class HorarioBasePermissionMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'gestion_especialistas.view_horariobase'

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar horarios base.")
        return super().handle_no_permission()

class HorarioBaseListView(LoginRequiredMixin, HorarioBasePermissionMixin, ListView):
    model = HorarioBase
    template_name = 'gestion_especialistas/horario_base/lista_horario_base.html'
    context_object_name = 'horarios_base'

class HorarioBaseCreateView(LoginRequiredMixin, HorarioBasePermissionMixin, CreateView):
    model = HorarioBase
    form_class = HorarioBaseForm
    template_name = 'gestion_especialistas/horario_base/crear_horario_base.html'
    success_url = reverse_lazy('gestion_especialistas:lista_horario_base')
    permission_required = 'gestion_especialistas.add_horariobase'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'✅ Horario base "{self.object.nombre}" creado exitosamente.') 
        return response
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"⚠️ Error en {field}: {error}")
        return super().form_invalid(form)

class HorarioBaseUpdateView(LoginRequiredMixin, HorarioBasePermissionMixin, UpdateView):
    model = HorarioBase
    form_class = HorarioBaseForm
    template_name = 'gestion_especialistas/horario_base/editar_horario_base.html'
    success_url = reverse_lazy('gestion_especialistas:lista_horario_base')
    permission_required = 'gestion_especialistas.change_horariobase'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'📝 Horario base "{self.object.nombre}" actualizado correctamente.')
        return response

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"⚠️ Error en {field}: {error}")
        return super().form_invalid(form)


class HorarioBaseDeleteView(LoginRequiredMixin, HorarioBasePermissionMixin, DeleteView):
    model = HorarioBase
    template_name = 'gestion_especialistas/horario_base/eliminar_horario_base.html'
    context_object_name = 'horario_base'
    success_url = reverse_lazy('gestion_especialistas:lista_horario_base')
    permission_required = 'gestion_especialistas.delete_horariobase' 

    def form_valid(self, form):
        messages.success(self.request, f'🗑️ Horario base "{self.object.nombre}" eliminado exitosamente.') 
        return super().form_valid(form)


# ------------------------------------
# Vistas CRUD para el Modelo Disponibilidad
# ------------------------------------

class DisponibilidadPermissionMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'gestion_especialistas.view_disponibilidad'

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para gestionar disponibilidades.")
        return super().handle_no_permission()

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

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"⚠️ Error en {field}: {error}")
        return super().form_invalid(form)


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

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"⚠️ Error en {field}: {error}")
        return super().form_invalid(form)


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