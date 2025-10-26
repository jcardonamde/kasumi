from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q

from .models import Rol, UsuarioRol, HistorialUsuario
from .forms import RolForm, AsignarRolForm, CambiarContrasenaForm, RestablecerContrasenaForm, UsuarioForm
from accounts.models import Usuario


# Vistas para la gestión de roles
class ListaRolesView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Vista para listar todos los roles."""
    model = Rol
    template_name = 'gestion_usuarios/roles/lista_roles.html'
    context_object_name = 'roles'
    paginate_by = 10
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', '').strip()
        
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )
        
        return queryset.order_by('nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Gestión de Roles')
        context['busqueda'] = self.request.GET.get('busqueda', '')
        return context


class CrearRolView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Vista para crear un nuevo rol."""
    model = Rol
    form_class = RolForm
    template_name = 'gestion_usuarios/roles/form_rol.html'
    success_url = reverse_lazy('gestion_usuarios:lista_roles')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Rol creado correctamente.'))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Crear Nuevo Rol')
        context['accion'] = _('Crear')
        return context


class EditarRolView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Vista para editar un rol existente."""
    model = Rol
    form_class = RolForm
    template_name = 'gestion_usuarios/roles/form_rol.html'
    success_url = reverse_lazy('gestion_usuarios:lista_roles')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Rol actualizado correctamente.'))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Editar Rol')
        context['accion'] = _('Actualizar')
        return context


class EliminarRolView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Vista para eliminar un rol."""
    model = Rol
    template_name = 'gestion_usuarios/roles/eliminar_rol.html'
    success_url = reverse_lazy('gestion_usuarios:lista_roles')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def delete(self, request, *args, **kwargs):
        rol = self.get_object()
        # Verificar si el rol está siendo usado
        if rol.usuarios_asignados.exists():
            messages.error(
                request, 
                _('No se puede eliminar el rol porque está asignado a uno o más usuarios.')
            )
            return redirect('gestion_usuarios:editar_rol', pk=rol.pk)
        
        messages.success(request, _('Rol eliminado correctamente.'))
        return super().delete(request, *args, **kwargs)


# Vistas para la gestión de usuarios
class ListaUsuariosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Vista para listar todos los usuarios."""
    model = Usuario
    template_name = 'gestion_usuarios/usuarios/lista_usuarios.html'
    context_object_name = 'usuarios'
    paginate_by = 15
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', '').strip()
        
        if busqueda:
            queryset = queryset.filter(
                Q(email__icontains=busqueda) |
                Q(first_name__icontains=busqueda) |
                Q(last_name__icontains=busqueda) |
                Q(numero_documento__icontains=busqueda)
            )
        
        return queryset.order_by('first_name', 'last_name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Gestión de Usuarios')
        context['busqueda'] = self.request.GET.get('busqueda', '')
        return context


class CrearUsuarioView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Vista para crear un nuevo usuario."""
    model = Usuario
    form_class = UsuarioForm
    template_name = 'gestion_usuarios/usuarios/form_usuario.html'
    success_url = reverse_lazy('gestion_usuarios:lista_usuarios')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_new'] = True
        return kwargs
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Usuario creado correctamente.'))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Crear Nuevo Usuario')
        context['accion'] = _('Crear')
        return context


class EditarUsuarioView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Vista para editar un usuario existente."""
    model = Usuario
    form_class = UsuarioForm
    template_name = 'gestion_usuarios/usuarios/form_usuario.html'
    success_url = reverse_lazy('gestion_usuarios:lista_usuarios')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['is_new'] = False
        return kwargs
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Usuario actualizado correctamente.'))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Editar Usuario')
        context['accion'] = _('Actualizar')
        return context


class EliminarUsuarioView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Vista para eliminar un usuario."""
    model = Usuario
    template_name = 'gestion_usuarios/usuarios/eliminar_usuario.html'
    success_url = reverse_lazy('gestion_usuarios:lista_usuarios')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def delete(self, request, *args, **kwargs):
        usuario = self.get_object()
        
        # No permitir que un usuario se elimine a sí mismo
        if usuario == request.user:
            messages.error(request, _('No puedes eliminar tu propio usuario.'))
            return redirect('gestion_usuarios:lista_usuarios')
        
        messages.success(request, _('Usuario eliminado correctamente.'))
        return super().delete(request, *args, **kwargs)


class DetalleUsuarioView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Vista para ver los detalles de un usuario."""
    model = Usuario
    template_name = 'gestion_usuarios/usuarios/detalle_usuario.html'
    context_object_name = 'usuario_detalle'
    
    def test_func(self):
        # Solo el propio usuario o un administrador pueden ver los detalles
        usuario = self.get_object()
        return self.request.user.is_staff or self.request.user == usuario
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Detalles del Usuario')
        context['usuario'] = self.request.user
        return context


class CambiarContrasenaView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Vista para que un usuario cambie su propia contraseña."""
    model = Usuario
    form_class = CambiarContrasenaForm
    template_name = 'gestion_usuarios/usuarios/cambiar_contrasena.html'
    
    def test_func(self):
        # Solo el propio usuario puede cambiar su contraseña
        usuario = self.get_object()
        return self.request.user == usuario
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Tu contraseña ha sido actualizada correctamente.'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('gestion_usuarios:detalle_usuario', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Cambiar Contraseña')
        return context


# Vistas para la asignación de roles
class AsignarRolView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Vista para asignar un rol a un usuario."""
    model = UsuarioRol
    form_class = AsignarRolForm
    template_name = 'gestion_usuarios/roles/asignar_rol.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_id = self.kwargs.get('usuario_id')
        context['usuario'] = get_object_or_404(Usuario, pk=usuario_id)
        context['titulo'] = _('Asignar Rol')
        return context
    
    def form_valid(self, form):
        usuario_id = self.kwargs.get('usuario_id')
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        
        # Verificar si ya tiene el rol asignado
        rol = form.cleaned_data['rol']
        if UsuarioRol.objects.filter(usuario=usuario, rol=rol).exists():
            messages.error(
                self.request, 
                _('El usuario ya tiene asignado este rol.')
            )
            return self.form_invalid(form)
        
        # Asignar el rol
        usuario_rol = form.save(commit=False)
        usuario_rol.usuario = usuario
        usuario_rol.asignado_por = self.request.user
        usuario_rol.save()
        
        messages.success(
            self.request, 
            _('Rol asignado correctamente al usuario.')
        )
        return redirect('gestion_usuarios:detalle_usuario', pk=usuario.pk)


class QuitarRolView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Vista para quitar un rol a un usuario."""
    model = UsuarioRol
    template_name = 'gestion_usuarios/roles/quitar_rol.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_success_url(self):
        return reverse_lazy(
            'gestion_usuarios:detalle_usuario', 
            kwargs={'pk': self.object.usuario.pk}
        )
    
    def delete(self, request, *args, **kwargs):
        messages.success(
            request, 
            _('Rol quitado correctamente del usuario.')
        )
        return super().delete(request, *args, **kwargs)
