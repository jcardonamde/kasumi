from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from .forms import LoginForm, UsuarioForm

class LoginView(View):
    """Vista para el inicio de sesión."""
    template_name = 'accounts/login.html'
    form_class = LoginForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Username es el email en nuestro caso
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, _('¡Bienvenido de nuevo!'))
                    next_url = request.GET.get('next', 'core:home')
                    return redirect(next_url)
                else:
                    messages.error(request, _('Tu cuenta está inactiva.'))
            else:
                messages.error(request, _('Correo o contraseña incorrectos.'))
        
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    """Vista para cerrar sesión."""
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _('Has cerrado sesión correctamente.'))
        return redirect('accounts:login')


@method_decorator(login_required, name='dispatch')
class PerfilView(TemplateView):
    """Vista para el perfil del usuario."""
    template_name = 'accounts/perfil.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context


# Vistas para la gestión de usuarios (solo para administradores)
@method_decorator(login_required, name='dispatch')
class ListaUsuariosView(TemplateView):
    """Vista para listar todos los usuarios (solo para administradores)."""
    template_name = 'accounts/lista_usuarios.html'
    
    def get_context_data(self, **kwargs):
        if not self.request.user.is_staff:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
            
        context = super().get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.all().order_by('first_name')
        return context


@method_decorator(login_required, name='dispatch')
class CrearUsuarioView(View):
    """Vista para crear un nuevo usuario (solo para administradores)."""
    template_name = 'accounts/form_usuario.html'
    form_class = UsuarioForm
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'accion': 'Crear'})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('Usuario creado correctamente.'))
            return redirect('accounts:editar_usuario', pk=user.pk)
        return render(request, self.template_name, {'form': form, 'accion': 'Crear'})


@method_decorator(login_required, name='dispatch')
class EditarUsuarioView(View):
    """Vista para editar un usuario existente (solo para administradores)."""
    template_name = 'accounts/form_usuario.html'
    form_class = UsuarioForm
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff and request.user.pk != kwargs.get('pk'):
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        from django.shortcuts import get_object_or_404
        from .models import Usuario
        
        usuario = get_object_or_404(Usuario, pk=kwargs.get('pk'))
        form = self.form_class(instance=usuario)
        return render(request, self.template_name, {
            'form': form, 
            'usuario': usuario,
            'accion': 'Editar'
        })
    
    def post(self, request, *args, **kwargs):
        from django.shortcuts import get_object_or_404
        from .models import Usuario
        
        usuario = get_object_or_404(Usuario, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance=usuario)
        
        if form.is_valid():
            form.save()
            messages.success(request, _('Usuario actualizado correctamente.'))
            return redirect('accounts:editar_usuario', pk=usuario.pk)
            
        return render(request, self.template_name, {
            'form': form, 
            'usuario': usuario,
            'accion': 'Editar'
        })
