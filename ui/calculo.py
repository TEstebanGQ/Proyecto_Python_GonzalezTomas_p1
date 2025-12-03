from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.formatting import print_error
from core.calculos import ( obtener_estadisticas_periodo, es_gasto_hoy, es_gasto_ultima_semana, es_gasto_mes_actual)
from ui.menuSystem import Menu


def mostrar_desglose_categorias(total, categorias):
    print("\nDesglose por categoría:")
    if categorias:
        for cat, monto in sorted(categorias.items()):
            print(f"  • {cat.capitalize()}: ${monto:.2f}")
    else:
        print("  No hay gastos registrados en este período.")


def vista_estadisticas_periodo(titulo, mensaje, filtro_func):
    limpiarPantalla()
    print(f"""
=============================================
              {titulo}
=============================================
""")
    try:
        estadisticas = obtener_estadisticas_periodo(filtro_func)
        
        print(f"{mensaje}: ${estadisticas['total']:.2f}")
        print(f"Cantidad de gastos: {estadisticas['cantidad_gastos']}")
        
        mostrar_desglose_categorias(
            estadisticas['total'], 
            estadisticas['por_categoria']
        )
        
        print("=" * 45)
    except Exception as e:
        print_error(f"Error al calcular estadísticas: {str(e)}")
    
    pausarPantalla()


def vista_total_diario():
    vista_estadisticas_periodo(
        'Total Diario',
        'Total gastado hoy',
        es_gasto_hoy )

def vista_total_semanal():
    vista_estadisticas_periodo(
        'Total Semanal',
        'Total gastado en los últimos 7 días',
        es_gasto_ultima_semana )

def vista_total_mensual():
    vista_estadisticas_periodo(
        'Total Mensual',
        'Total gastado este mes',
        es_gasto_mes_actual )

def menu_calculos():
    opciones = [
        {'texto': 'Calcular total diario', 'accion': vista_total_diario},
        {'texto': 'Calcular total semanal', 'accion': vista_total_semanal},
        {'texto': 'Calcular total mensual', 'accion': vista_total_mensual},
        {'texto': 'Regresar al menú principal', 'accion': lambda: False}
    ]
    
    menu = Menu("Calcular Total de Gastos", opciones)
    menu.mostrar()