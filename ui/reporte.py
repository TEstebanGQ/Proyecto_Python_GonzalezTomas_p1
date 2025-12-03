from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.formatting import print_success, print_error
from core.reportes import ( reporte_diario, reporte_semanal, reporte_mensual, guardar_reporte_json, formatear_reporte_texto)
from ui.menuSystem import Menu

def mostrar_reporte_pantalla(reporte):
    limpiarPantalla()
    print(f"""
=============================================
         Reporte {reporte['tipo'].capitalize()}
=============================================
""")
    
    # Usar el formateador centralizado
    texto_reporte = formatear_reporte_texto(reporte)
    print(texto_reporte)
    
    print("\n" + "="*45)
    pausarPantalla()


def guardar_reporte_archivo(reporte, nombre_archivo):
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
        print(f"Tipo: {reporte['tipo'].capitalize()}")
        print(f"Total: ${reporte['total']:.2f}")
        print("="*45)
    except Exception as e:
        print_error(f"Error al guardar el reporte: {str(e)}")
    
    pausarPantalla()


def crear_submenu_reporte(nombre_tipo, nombre_archivo, funcion_reporte):
    def submenu():
        try:
            # Generar el reporte una sola vez
            reporte = funcion_reporte()
            
            opciones = [
                {
                    'texto': 'Mostrar en pantalla',
                    'accion': lambda: mostrar_reporte_pantalla(reporte)
                },
                {
                    'texto': 'Guardar como JSON',
                    'accion': lambda: guardar_reporte_archivo(reporte, nombre_archivo)
                },
                {
                    'texto': 'Regresar',
                    'accion': lambda: False
                }
            ]
            
            menu = Menu(f"Reporte {nombre_tipo}", opciones)
            menu.mostrar()
            
        except Exception as e:
            limpiarPantalla()
            print_error(f"Error al generar el reporte: {str(e)}")
            pausarPantalla()
    
    return submenu


# Crear las vistas específicas usando el generador
vista_reporte_diario = crear_submenu_reporte(
    "Diario",
    "reporte_diario",
    reporte_diario
)

vista_reporte_semanal = crear_submenu_reporte(
    "Semanal",
    "reporte_semanal",
    reporte_semanal
)

vista_reporte_mensual = crear_submenu_reporte(
    "Mensual",
    "reporte_mensual",
    reporte_mensual
)


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