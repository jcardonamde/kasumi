from django.urls import path
from .views import ConfiguracionesHomeView

app_name = "configuraciones"

urlpatterns = [
    path('', ConfiguracionesHomeView.as_view(), name='index'),
]
