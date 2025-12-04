from ui.prompts import inputSeguro
from utils.screenControllers import limpiarPantalla, pausarPantalla
from core.storage import loadData
from core.reportes import totalDiario, totalSemanal, totalMensual

def calcularTotalesMenu():
    data = loadData()
    gastos = data["gastos"]

    limpiarPantalla()
    print("""
=============================================
          Calcular Total de Gastos
=============================================
Seleccione el periodo de cálculo:

1. Calcular total diario
2. Calcular total semanal
3. Calcular total mensual
4. Regresar al menú principal
=============================================
""")

    opcion = inputSeguro("Seleccione una opción: ")

    if opcion == "1":
        calcularTotalDiario(gastos)
    elif opcion == "2":
        calcularTotalSemanal(gastos)
    elif opcion == "3":
        calcularTotalMensual(gastos)
    elif opcion == "4":
        return
    else:
        print("Opción inválida.")
    
    pausarPantalla()

def calcularTotalDiario(gastos):
    total = totalDiario(gastos)
    print(f"\n Total diario: ${total:.2f}")

def calcularTotalSemanal(gastos):
    total = totalSemanal(gastos)
    print(f"\n Total semanal (últimos 7 días): ${total:.2f}")

def calcularTotalMensual(gastos):
    total = totalMensual(gastos)
    print(f"\n Total mensual: ${total:.2f}")