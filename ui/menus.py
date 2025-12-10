from ui.prompts import confirmarAccion
from utils.screenControllers import limpiarPantalla
from utils.menu import menu
from core.gastoManager import registrarGasto
from ui.listado import listarGastosMenu
from ui.calculos import calcularTotalesMenu
from ui.reporte import generarReporteMenu

def menuPrincipal():
    opciones = (
        "Registrar nuevo gasto",
        "Listar gastos",
        "Calcular total de gastos",
        "Generar reporte de gastos",
        "Salir"
    )
    
    while True:
        limpiarPantalla()
        opcion = menu("Simulador de Gasto Diario", opciones)
        
        match opcion:
            case 1:
                registrarGasto()
            case 2:
                listarGastosMenu()
            case 3:
                calcularTotalesMenu()
            case 4:
                generarReporteMenu()
            case 5:
                if confirmarAccion("¿Desea salir del programa? (S/N): "):
                    print("\nGracias por usar el Simulador de Gasto Diario.")
                    break
