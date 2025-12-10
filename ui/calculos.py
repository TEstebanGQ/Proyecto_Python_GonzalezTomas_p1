from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.menu import menu
from core.storage import loadData
from core.reportes import totalDiario, totalSemanal, totalMensual

def calcularTotalesMenu():
    opciones = (
        "Calcular total diario",
        "Calcular total semanal",
        "Calcular total mensual",
        "Regresar al menú principal"
    )
    
    while True:
        data = loadData()
        gastos = data["gastos"]

        limpiarPantalla()
        opcion = menu("Calcular Total de Gastos", opciones)
        
        match opcion:
            case 1:
                calcularTotalDiario(gastos)
                pausarPantalla()
            case 2:
                calcularTotalSemanal(gastos)
                pausarPantalla()
            case 3:
                calcularTotalMensual(gastos)
                pausarPantalla()
            case 4:
                break

def calcularTotalDiario(gastos):
    total = totalDiario(gastos)
    print(f"\n Total diario: ${total:.2f}")

def calcularTotalSemanal(gastos):
    total = totalSemanal(gastos)
    print(f"\n Total semanal (últimos 7 días): ${total:.2f}")

def calcularTotalMensual(gastos):
    total = totalMensual(gastos)
    print(f"\n Total mensual: ${total:.2f}")