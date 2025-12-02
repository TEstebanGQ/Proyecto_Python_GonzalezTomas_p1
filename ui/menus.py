from utils.screenControllers import limpiarPantalla, pausarPantalla
from core.gastoManager import registrar_gasto, listar_gastos
from core.calculos import total_diario, total_semanal, total_mensual
from core.reportes import generar_reporte


def menu_principal():
    while True:
        limpiarPantalla()
        print("""
=============================================
       Simulador de Gasto Diario
=============================================
1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte
5. Salir
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_registro()
        elif opcion == "2":
            menu_listar()
        elif opcion == "3":
            menu_calculos()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            print("Saliendo del programa...")
            pausarPantalla()
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            pausarPantalla()


# --- MENÚ REGISTRO -------------------------

def menu_registro():
    limpiarPantalla()
    print("=== Registrar Gasto ===")
    registrar_gasto()
    pausarPantalla()


# --- MENÚ LISTAR ---------------------------

def menu_listar():
    limpiarPantalla()
    print("=== Listar Gastos ===")
    listar_gastos()
    pausarPantalla()


# --- MENÚ CÁLCULOS -------------------------

def menu_calculos():
    while True:
        limpiarPantalla()
        print("""
=============================================
          Calcular Total de Gastos
=============================================
1. Total diario
2. Total semanal
3. Total mensual
4. Regresar
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            total_diario()
        elif opcion == "2":
            total_semanal()
        elif opcion == "3":
            total_mensual()
        elif opcion == "4":
            return
        else:
            print("Opción inválida.")

        pausarPantalla()


# --- MENÚ REPORTES --------------------------

def menu_reportes():
    while True:
        limpiarPantalla()
        print("""
=============================================
           Generar Reporte de Gastos
=============================================
1. Reporte diario
2. Reporte semanal
3. Reporte mensual
4. Regresar
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion in ["1", "2", "3"]:
            generar_reporte(opcion)
        elif opcion == "4":
            return
        else:
            print("Opción inválida.")

        pausarPantalla()