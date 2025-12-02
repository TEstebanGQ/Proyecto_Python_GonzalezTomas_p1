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
def generar_reporte(tipo_opcion):
    """
    Genera un reporte según la opción seleccionada
    tipo_opcion: "1" para diario, "2" para semanal, "3" para mensual
    """
    if tipo_opcion == "1":
        reporte = reporte_diario()
        nombre = "reporte_diario"
    elif tipo_opcion == "2":
        reporte = reporte_semanal()
        nombre = "reporte_semanal"
    elif tipo_opcion == "3":
        reporte = reporte_mensual()
        nombre = "reporte_mensual"
    else:
        print("Opción inválida")
        return
    
    # Mostrar el reporte
    print(f"\n=== Reporte {reporte['tipo'].upper()} ===")
    print(f"Total: ${reporte['total']:.2f}")
    print("\nPor categoría:")
    for cat, monto in reporte['por_categoria'].items():
        print(f"  - {cat}: ${monto:.2f}")
    
    # Guardar el reporte
    ruta = guardar_reporte_json(reporte, nombre)
    print(f"\nReporte guardado en: {ruta}")
