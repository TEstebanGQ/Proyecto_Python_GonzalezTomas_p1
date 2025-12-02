from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.formatting import print_error
from core.calculos import total_diario, total_semanal, total_mensual, totales_por_categoria
from ui.menuSystem import Menu


def mostrar_desglose_categorias(total, categorias):
    """Muestra el desglose por categoría con porcentajes"""
    print("Desglose por categoría:")
    if categorias:
        for cat, monto in categorias.items():
            porcentaje = (monto / total * 100) if total > 0 else 0
            print(f"  • {cat.capitalize()}: ${monto:.2f} ({porcentaje:.1f}%)")
    else:
        print("  No hay gastos registrados en este período.")


def vista_total_diario():
    """Vista para mostrar el total diario"""
    limpiarPantalla()
    print("""
=============================================
              Total Diario
=============================================
""")
    try:
        total = total_diario()
        print(f"Total gastado hoy: ${total:.2f}\n")
        
        categorias = totales_por_categoria()
        mostrar_desglose_categorias(total, categorias)
        print("="*45)
    except Exception as e:
        print_error(f"Error al calcular total diario: {str(e)}")
    
    pausarPantalla()


def vista_total_semanal():
    """Vista para mostrar el total semanal"""
    limpiarPantalla()
    print("""
=============================================
              Total Semanal
=============================================
""")
    try:
        total = total_semanal()
        print(f"Total gastado en los últimos 7 días: ${total:.2f}\n")
        
        categorias = totales_por_categoria()
        mostrar_desglose_categorias(total, categorias)
        print("="*45)
    except Exception as e:
        print_error(f"Error al calcular total semanal: {str(e)}")
    
    pausarPantalla()


def vista_total_mensual():
    """Vista para mostrar el total mensual"""
    limpiarPantalla()
    print("""
=============================================
              Total Mensual
=============================================
""")
    try:
        total = total_mensual()
        print(f"Total gastado este mes: ${total:.2f}\n")
        
        categorias = totales_por_categoria()
        mostrar_desglose_categorias(total, categorias)
        print("="*45)
    except Exception as e:
        print_error(f"Error al calcular total mensual: {str(e)}")
    
    pausarPantalla()


def menu_calculos():
    """Menú principal para calcular totales"""
    opciones = [
        {'texto': 'Calcular total diario', 'accion': vista_total_diario},
        {'texto': 'Calcular total semanal', 'accion': vista_total_semanal},
        {'texto': 'Calcular total mensual', 'accion': vista_total_mensual},
        {'texto': 'Regresar al menú principal', 'accion': lambda: False}
    ]
    
    menu = Menu("Calcular Total de Gastos", opciones)
    menu.mostrar()