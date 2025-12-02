import json
from core.calculos import total_diario, total_semanal, total_mensual, totales_por_categoria
from data.storage import save_report


def reporte_diario():
    return _reporte_base('diario', total_diario(), totales_por_categoria())


def reporte_semanal():
    return _reporte_base('semanal', total_semanal(), totales_por_categoria())


def reporte_mensual():
    return _reporte_base('mensual', total_mensual(), totales_por_categoria())


def _reporte_base(tipo, total, por_categoria):
    reporte = {
        'tipo': tipo,
        'total': total,
        'por_categoria': por_categoria
    }
    return reporte


def guardar_reporte_json(reporte, nombre_archivo):
    return save_report(reporte, nombre_archivo)
