from ui.prompts import inputSeguro, confirmarAccion
from utils.screenControllers import limpiarPantalla, pausarPantalla
from core.storage import loadData
from core.proyeccion import generarProyeccion, guardarProyeccion
from tabulate import tabulate

def validarDiasFuturos(diasStr):
    try:
        dias = int(diasStr)
        if dias <= 0:
            print(" Error: El número de días debe ser mayor a 0.")
            return None
        if dias > 365:
            print("Error: Solo es posible entre el rango de 1  a 365 dias")
            return None
        return dias
    except ValueError:
        print(" Error: Debe ingresar un número entero válido.")
        return None

def proyeccionGastoMenu():
    limpiarPantalla()
    print("""
==================================================
        Proyección de Gastos Futuros
==================================================
""")

    while True:
        diasInput = inputSeguro("\n¿Para cuántos días desea proyectar? (1-365): ")
        if diasInput is None:
            print(" Operación cancelada.")
            pausarPantalla()
            return
        
        diasFuturos = validarDiasFuturos(diasInput)
        if diasFuturos is not None:
            break

    data = loadData()
    gastos = data["gastos"]
    
    if not gastos:
        print("\n No hay gastos registrados para generar una proyección.")
        pausarPantalla()
        return
    
    print("\n Generando proyección...")
    proyeccion = generarProyeccion(gastos, diasFuturos)
    
    if "error" in proyeccion:
        print(f"\n {proyeccion['error']}")
        print(f" Gastos disponibles: {proyeccion['datosDisponibles']}")
        print("\n Se necesitan al menos algunos gastos registrados para generar una proyección.")
        pausarPantalla()
        return
    mostrarProyeccion(proyeccion)
 
    if confirmarAccion("\n¿Desea guardar esta proyección en un archivo JSON? (S/N): "):
        try:
            archivo = guardarProyeccion(proyeccion)
            print(f" Proyección guardada exitosamente en: {archivo}")
        except Exception as e:
            print(f" Error al guardar: {e}")
    
    pausarPantalla()

def mostrarProyeccion(proyeccion):
    limpiarPantalla()
    print("""
=============================================
           PROYECCIÓN DE GASTOS
=============================================
""")
    p = proyeccion['proyeccion']
    print(f"=== Proyección para los próximos {p['diasProyectados']} días ===")
    print(f"\n GASTO TOTAL PROYECTADO: ${p['gastoTotalProyectado']:.2f}")

    if p['categoriasOrdenadas']:
        print("\n=== Proyección por Categoría ===")
        tablaCategorias = [
            [
                cat['categoria'].capitalize(),
                f"${cat['montoProyectado']:.2f}"
            ]
            for cat in p['categoriasOrdenadas']
        ]
        print(tabulate(
            tablaCategorias,
            headers=["Categoría", "Monto Proyectado"],
            tablefmt="grid"
        ))