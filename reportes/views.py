from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from gestion_usuarios.models import Rol 
from . import utils 
import logging

logger = logging.getLogger(__name__)


def lista_reportes(request):
    """Muestra la interfaz de selección de filtros y tipos de reportes."""
    
    try:
        roles_generales = Rol.objects.all().order_by('nombre')
    except Exception:
        roles_generales = []
        logger.exception("Error al obtener roles en lista_reportes.")
    
    context = {
        'roles_generales': roles_generales
    }
    
    return render(request, 'reportes/lista_reportes.html', context)


def generar_reporte_usuarios(request):
    """Genera el reporte de usuarios en formato Excel o PDF."""
    
    fecha_inicial = request.GET.get('fecha_inicial')
    fecha_final = request.GET.get('fecha_final')
    rol_id = request.GET.get('rol')
    formato = request.GET.get('formato')
    
    try:
        if formato in ['excel', 'excel_imprimir']:
            return utils.generar_excel_usuarios(fecha_inicial, fecha_final, rol_id)
            
        elif formato in ['pdf', 'pdf_imprimir']:
            return utils.generar_pdf_usuarios(fecha_inicial, fecha_final, rol_id, formato)
        
        return HttpResponseBadRequest("Formato de reporte no válido.")
    
    except Exception as e:
        logger.exception("Error fatal generando reporte de usuarios.")
        return HttpResponse(f"Error interno del servidor al generar el reporte de usuarios. Detalle: {e}", status=500)


def generar_reporte_clientes(request):
    """Genera el reporte de clientes en formato Excel (XLSX) o PDF."""
    
    fecha_inicial = request.GET.get('fecha_inicial')
    fecha_final = request.GET.get('fecha_final')
    formato = request.GET.get('formato')
    
    try:
        if formato in ['excel', 'excel_imprimir']:
            return utils.generar_excel_clientes(fecha_inicial, fecha_final)
            
        elif formato in ['pdf', 'pdf_imprimir']:
            return utils.generar_pdf_clientes(fecha_inicial, fecha_final, formato)
        
        return HttpResponseBadRequest("Formato de reporte no válido.")
        
    except Exception as e:
        logger.exception("Error fatal generando reporte de clientes.")
        return HttpResponse(f"Error interno al generar el reporte de CLIENTES. Detalle: {e}", status=500)


def generar_reporte_servicios(request):
    """Genera el reporte de servicios en formato Excel (XLSX) o PDF."""
    
    formato = request.GET.get('formato')
    
    try:
        if formato in ['excel', 'excel_imprimir']:
            return utils.generar_excel_servicios() 
            
        elif formato in ['pdf', 'pdf_imprimir']:
            return utils.generar_pdf_servicios(formato)
        
        return HttpResponseBadRequest("Formato de reporte no válido.")
        
    except Exception as e:
        logger.exception("Error fatal generando reporte de servicios.")
        return HttpResponse(f"Error interno al generar el reporte de Servicios. Detalle: {e}", status=500)


def generar_reporte_especialistas(request):
    """
    Genera el reporte de especialistas en formato Excel (XLSX) o PDF, 
    filtrando por rango de fecha de registro.
    """
    fecha_inicial = request.GET.get('fecha_inicial')
    fecha_final = request.GET.get('fecha_final')
    formato = request.GET.get('formato')

    try:
        if formato in ['excel', 'excel_imprimir']:
            return utils.generar_excel_especialistas(fecha_inicial, fecha_final)
        
        elif formato in ['pdf', 'pdf_imprimir']:
            return utils.generar_pdf_especialistas(fecha_inicial, fecha_final, formato)
            
        return HttpResponseBadRequest("Formato de reporte no válido.")
        
    except Exception as e:
        logger.exception("Error fatal generando reporte de especialistas.")
        return HttpResponse(f"Error interno al generar el reporte de ESPECIALISTAS. Detalle: {e}", status=500)


def generar_reporte_citas(request):
    """
    Genera el reporte de citas agendadas en formato Excel o PDF, 
    filtrando por rango de fecha y hora.
    """
    fecha_inicial = request.GET.get('fecha_inicial')
    fecha_final = request.GET.get('fecha_final')
    formato = request.GET.get('formato')
    
    try:
        if formato in ['excel', 'excel_imprimir']:
            return utils.generar_excel_citas(fecha_inicial, fecha_final)

        elif formato in ['pdf', 'pdf_imprimir', 'inline']:
            return utils.generar_pdf_citas(fecha_inicial, fecha_final, formato)
        
        return HttpResponseBadRequest("Formato de reporte no válido.")

    except Exception as e:
        logger.exception("Error fatal generando reporte de citas.")
        return HttpResponse(f"Error interno al generar el reporte de CITAS. Detalle: {e}", status=500)


def generar_reporte_agenda(request):
    """
    Genera el reporte de Agenda General (Disponibilidad y Citas) en formato PDF.
    Requiere fechas inicial y final.
    """
    fecha_inicial = request.GET.get('fecha_inicial')
    fecha_final = request.GET.get('fecha_final')
    formato = request.GET.get('formato')
    
    if formato not in ['pdf', 'pdf_imprimir', 'inline']:
        return HttpResponseBadRequest("El reporte de Agenda General solo se puede generar en formato PDF.")

    if not fecha_inicial or not fecha_final:
        return HttpResponseBadRequest("Se deben especificar las fechas inicial y final para el Reporte de Agenda General.")

    try:
        return utils.generar_pdf_agenda_general(fecha_inicial, fecha_final, formato)
        
    except Exception as e:
        logger.exception("Error fatal generando reporte de agenda general.")
        return HttpResponse(f"Error interno al generar el reporte de AGENDA GENERAL. Detalle: {e}", status=500)