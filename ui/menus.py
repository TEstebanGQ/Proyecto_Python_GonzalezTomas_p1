from ui.prompts import inputSeguro, confirmarAccion
from utils.screenControllers import limpiarPantalla, pausarPantalla
from core.gastoManager import registrarGasto
from ui.listado import listarGastosMenu
from ui.calculos import calcularTotalesMenu
from ui.reporte import generarReporteMenu

def menuPrincipal():
    while True:
        limpiarPantalla()
        print("""
=============================================
        Simulador de Gasto Diario
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Salir
=============================================
""")

        opcion = inputSeguro("Seleccione una opción: ")

        if opcion == "1":
            registrarGasto()
        elif opcion == "2":
            listarGastosMenu()
        elif opcion == "3":
            calcularTotalesMenu()
        elif opcion == "4":
            generarReporteMenu()
        elif opcion == "5":
            if confirmarAccion("¿Desea salir del programa? (S/N): "):
                print("\nGracias por usar el Simulador de Gasto Diario.")
                break
        else:
            print("Opción inválida.")
            pausarPantalla()