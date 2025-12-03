from core.calculos import (
    obtener_estadisticas_periodo,
    es_gasto_hoy,
    es_gasto_ultima_semana,
    es_gasto_mes_actual
)
from data.storage import save_report


def generar_reporte(tipo, filtro_func):
    estadisticas = obtener_estadisticas_periodo(filtro_func)
    
    return {
        'tipo': tipo,
        'total': estadisticas['total'],
        'por_categoria': estadisticas['por_categoria'],
        'cantidad_gastos': estadisticas['cantidad_gastos']
    }


def reporte_diario():
    return generar_reporte('diario', es_gasto_hoy)


def reporte_semanal():
    return generar_reporte('semanal', es_gasto_ultima_semana)


def reporte_mensual():
    return generar_reporte('mensual', es_gasto_mes_actual)


def guardar_reporte_json(reporte, nombre_archivo):
    return save_report(reporte, nombre_archivo)


def formatear_reporte_texto(reporte):
    lineas = []
    lineas.append(f"=== Reporte {reporte['tipo'].upper()} ===")
    lineas.append(f"Total: ${reporte['total']:.2f}")
    lineas.append(f"Cantidad de gastos: {reporte.get('cantidad_gastos', 0)}")
    lineas.append("\nPor categoría:")
    
    if reporte['por_categoria']:
        for cat, monto in sorted(reporte['por_categoria'].items()):
            porcentaje = (monto / reporte['total'] * 100) if reporte['total'] > 0 else 0
            lineas.append(f"  - {cat.capitalize()}: ${monto:.2f} ({porcentaje:.1f}%)")
    else:
        lineas.append("  No hay gastos en este período")
    
    return '\n'.join(lineas)