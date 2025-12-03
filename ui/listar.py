from datetime import datetime
from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.formatting import mostrar_tabla_gastos, print_error
from core.gastoManager import listar_gastos
from core.validators import obtener_categorias_usadas
from ui.menuSystem import Menu


def vista_listar_todos():
    """Vista para listar todos los gastos"""
    limpiarPantalla()
    print("=== Todos los Gastos ===\n")
    gastos = listar_gastos()
    
    if not gastos:
        print("No hay gastos registrados aún.")
    else:
        mostrar_tabla_gastos(gastos)
    
    pausarPantalla()


def vista_listar_por_categoria():
    """Vista para filtrar gastos por categoría"""
    limpiarPantalla()
    print("=== Filtrar por Categoría ===\n")
    
    # Obtener categorías dinámicamente
    categorias = obtener_categorias_usadas()
    
    if not categorias:
        print("No hay categorías registradas aún.")
        pausarPantalla()
        return
    
    print("Categorías disponibles:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat.capitalize()}")
    
    print()
    cat_opcion = input("Seleccione una categoría: ").strip()
    
    try:
        opcion_num = int(cat_opcion)
        
        if 1 <= opcion_num <= len(categorias):
            categoria_filtro = categorias[opcion_num - 1]
            gastos = listar_gastos(lambda g: g['categoria'] == categoria_filtro)
            
            limpiarPantalla()
            print(f"=== Gastos en categoría: {categoria_filtro.upper()} ===\n")
            
            if not gastos:
                print(f"No hay gastos en la categoría '{categoria_filtro}'.")
            else:
                print(f"Total de gastos encontrados: {len(gastos)}\n")
                mostrar_tabla_gastos(gastos)
        else:
            print("Opción inválida.")
    except ValueError:
        print("Por favor ingrese un número válido.")
        
    pausarPantalla()


def vista_listar_por_fechas():
    """Vista para filtrar gastos por rango de fechas"""
    limpiarPantalla()
    print("=== Filtrar por Rango de Fechas ===\n")
    print("Ingrese las fechas en formato: YYYY-MM-DD")
    fecha_inicio = input("Fecha de inicio: ").strip()
    fecha_fin = input("Fecha de fin: ").strip()
    
    try:
        inicio = datetime.fromisoformat(fecha_inicio)
        fin = datetime.fromisoformat(fecha_fin)
        
        # Ajustar fin al final del día
        fin = fin.replace(hour=23, minute=59, second=59)
        
        gastos = listar_gastos(
            lambda g: inicio <= datetime.fromisoformat(g['fecha'].split('.')[0]) <= fin
        )
        
        limpiarPantalla()
        print(f"=== Gastos del {fecha_inicio} al {fecha_fin} ===\n")
        
        if not gastos:
            print("No hay gastos en el rango de fechas especificado.")
        else:
            print(f"Total de gastos encontrados: {len(gastos)}\n")
            mostrar_tabla_gastos(gastos)
            
            # Mostrar total
            total = sum(g['monto'] for g in gastos)
            print(f"\nTotal en el período: ${total:.2f}")
            
    except ValueError:
        print_error("Formato de fecha inválido. Use YYYY-MM-DD")
    pausarPantalla()

def menu_listar_gastos():
    """Menú principal para listar gastos"""
    opciones = [
        {'texto': 'Ver todos los gastos', 'accion': vista_listar_todos},
        {'texto': 'Filtrar por categoría', 'accion': vista_listar_por_categoria},
        {'texto': 'Filtrar por rango de fechas', 'accion': vista_listar_por_fechas},
        {'texto': 'Regresar al menú principal', 'accion': lambda: False}
    ]
    
    menu = Menu("Listar Gastos", opciones)
    menu.mostrar()