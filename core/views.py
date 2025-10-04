from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _

class HomeView(LoginRequiredMixin, TemplateView):
    """Vista para el dashboard principal."""
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Inicio')
        context['usuario'] = self.request.user
        # Aquí podrías agregar más datos para el dashboard
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Vista para el dashboard principal que muestra estadísticas y resúmenes.
    Esta es una versión más completa que podría crecer con el tiempo.
    """
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Datos básicos del usuario
        context['usuario'] = user
        context['titulo'] = _('Dashboard')
        
        # Aquí podrías agregar lógica para obtener estadísticas, como:
        # - Número de clientes
        # - Citas del día
        # - Ingresos del mes
        # - Próximas citas
        
        # Ejemplo de datos estáticos (reemplazar con consultas reales)
        context['estadisticas'] = {
            'total_clientes': 0,
            'citas_hoy': 0,
            'ingresos_mes': 0,
            'proximas_citas': []
        }
        
        return context
