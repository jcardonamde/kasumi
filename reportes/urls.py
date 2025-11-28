from django.urls import path
from . import views 

app_name = 'reportes'

urlpatterns = [
    path(
        '', 
        views.lista_reportes, 
        name='lista_reportes'
    ),
    
    path(
        'generar/usuarios/', 
        views.generar_reporte_usuarios, 
        name='generar_reporte_usuarios' 
    ),

    path(
        'generar/clientes/', 
        views.generar_reporte_clientes, 
        name='generar_reporte_clientes' 
    ),

    path(
        'generar/servicios/', 
        views.generar_reporte_servicios, 
        name='generar_reporte_servicios' 
    ),
    
    path(
        'generar/especialistas/', 
        views.generar_reporte_especialistas, 
        name='generar_reporte_especialistas' 
    ),

    path(
        'generar/citas/', 
        views.generar_reporte_citas, 
        name='generar_reporte_citas' 
    ),
    
    path(
        'generar/agenda/', 
        views.generar_reporte_agenda, 
        name='generar_reporte_agenda' 
    ),
]