from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.formatting import print_success, print_error
from core.reportes import reporte_diario, reporte_semanal, reporte_mensual, guardar_reporte_json
from ui.menuSystem import Menu


def mostrar_reporte_pantalla(reporte, nombre_tipo):
    """Muestra un reporte en pantalla"""
    limpiarPantalla()
    print(f"""
=============================================
         Reporte {nombre_tipo} - Pantalla
=============================================
""")
    print(f"Total: ${reporte['total']:.2f}\n")
    
    if reporte['por_categoria']:
        print("Desglose por categoría:")
        for cat, monto in reporte['por_categoria'].items():
            porcentaje = (monto / reporte['total'] * 100) if reporte['total'] > 0 else 0
            print(f"  • {cat.capitalize()}: ${monto:.2f} ({porcentaje:.1f}%)")
    else:
        print("No hay gastos en este período.")
    
    print("="*45)
    pausarPantalla()


def guardar_reporte_archivo(reporte, nombre_archivo):
    """Guarda un reporte en archivo JSON"""
    limpiarPantalla()
    print("""
=============================================
         Guardar Reporte
=============================================
""")
    
    try:
        ruta = guardar_reporte_json(reporte, nombre_archivo)
        print_success("¡Reporte guardado exitosamente!")
        print(f"\nUbicación: {ruta}")
        print("="*45)
    except Exception as e:
        print_error(f"Error al guardar el reporte: {str(e)}")
    
    pausarPantalla()


def submenu_reporte(tipo_reporte, nombre_tipo, nombre_archivo, funcion_reporte):
    """Submenú genérico para gestionar un reporte"""
    try:
        reporte = funcion_reporte()
        
        opciones = [
            {'texto': 'Mostrar en pantalla', 'accion': lambda: mostrar_reporte_pantalla(reporte, nombre_tipo)},
            {'texto': 'Guardar como JSON', 'accion': lambda: guardar_reporte_archivo(reporte, nombre_archivo)},
            {'texto': 'Regresar', 'accion': lambda: False}
        ]
        
        menu = Menu(f"Reporte {nombre_tipo}", opciones)
        menu.mostrar()
        
    except Exception as e:
        print_error(f"Error al generar el reporte: {str(e)}")
        pausarPantalla()


def vista_reporte_diario():
    """Vista para el reporte diario"""
    submenu_reporte("diario", "Diario", "reporte_diario", reporte_diario)


def vista_reporte_semanal():
    """Vista para el reporte semanal"""
    submenu_reporte("semanal", "Semanal", "reporte_semanal", reporte_semanal)


def vista_reporte_mensual():
    """Vista para el reporte mensual"""
    submenu_reporte("mensual", "Mensual", "reporte_mensual", reporte_mensual)


def menu_reportes():
    """Menú principal para generar reportes"""
    opciones = [
        {'texto': 'Reporte diario', 'accion': vista_reporte_diario},
        {'texto': 'Reporte semanal', 'accion': vista_reporte_semanal},
        {'texto': 'Reporte mensual', 'accion': vista_reporte_mensual},
        {'texto': 'Regresar al menú principal', 'accion': lambda: False}
    ]
    
    menu = Menu("Generar Reporte de Gastos", opciones)
    menu.mostrar()