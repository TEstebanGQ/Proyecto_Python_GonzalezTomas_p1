from ui.menuSystem import Menu, mostrar_confirmacion
from ui.gasto import vista_registro_gasto
from ui.listar import menu_listar_gastos
from ui.calculo import menu_calculos
from ui.reporte import menu_reportes


def confirmar_salida():
    """Confirma si el usuario desea salir del programa"""
    if mostrar_confirmacion("¿Desea salir del programa?"):
        print("Saliendo del programa...")
        exit()


def menu_principal():
    """Menú principal de la aplicación"""
    opciones = [
        {'texto': 'Registrar nuevo gasto', 'accion': vista_registro_gasto},
        {'texto': 'Listar gastos', 'accion': menu_listar_gastos},
        {'texto': 'Calcular total de gastos', 'accion': menu_calculos},
        {'texto': 'Generar reporte de gastos', 'accion': menu_reportes},
        {'texto': 'Salir', 'accion': confirmar_salida}
    ]
    
    menu = Menu("Simulador de Gasto Diario", opciones)
    menu.mostrar()