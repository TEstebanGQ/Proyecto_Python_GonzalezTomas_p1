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

def vista_total_generico(tipo, funcion_total, titulo, mensaje):
    limpiarPantalla()
    print(f"""
=============================================
              {titulo}
=============================================
""")
    try:
        total = funcion_total()
        print(f"{mensaje}: ${total:.2f}\n")
        categorias = totales_por_categoria()  # Nota: Aquí hay otra optimización posible, pasar filtro de período
        mostrar_desglose_categorias(total, categorias)
        print("="*45)
    except Exception as e:
        print_error(f"Error al calcular {tipo}: {str(e)}")
    pausarPantalla()

def vista_total_diario():
    vista_total_generico('diario', total_diario, 'Total Diario', 'Total gastado hoy')

def vista_total_semanal():
    vista_total_generico('semanal', total_semanal, 'Total Semanal', 'Total gastado en los últimos 7 días')

def vista_total_mensual():
    vista_total_generico('mensual', total_mensual, 'Total Mensual', 'Total gastado este mes')

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