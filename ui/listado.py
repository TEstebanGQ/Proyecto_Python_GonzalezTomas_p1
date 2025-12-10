from ui.prompts import inputSeguro
from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.menu import menu
from core.storage import loadData
from core.filtros import filtrarCategoria, filtrarRangoFechas
from utils.validators import validarFecha
from tabulate import tabulate

def listarGastosMenu():
    opciones = (
        "Ver todos los gastos",
        "Filtrar por categoría",
        "Filtrar por rango de fechas",
        "Regresar al menú principal"
    )
    
    data = loadData()
    gastos = data["gastos"]

    while True:
        limpiarPantalla()
        opcion = menu("Listar Gastos", opciones)
        
        match opcion:
            case 1:
                mostrarTabla(gastos)
            case 2:
                filtrarPorCategoriaUI(data, gastos)
            case 3:
                filtrarPorFechasUI(gastos)
            case 4:
                break

def filtrarPorCategoriaUI(data, gastos):
    limpiarPantalla()
    if not data["categorias"]:
        print(" No hay categorías disponibles.")
        pausarPantalla()
        return
        
    print("\nCategorías disponibles:")
    for idx, cat in enumerate(data["categorias"], start=1):
        print(f"  {idx}. {cat.capitalize()}")
    
    cat_num = inputSeguro("\nSeleccione el número de categoría: ")
    try:
        cat_idx = int(cat_num) - 1
        if 0 <= cat_idx < len(data["categorias"]):
            cat = data["categorias"][cat_idx]
            lista = filtrarCategoria(gastos, cat)
            mostrarTabla(lista)
        else:
            print(" Opción inválida.")
            pausarPantalla()
    except ValueError:
        print(" Debe ingresar un número válido.")
        pausarPantalla()

def filtrarPorFechasUI(gastos):
    limpiarPantalla()
    inicio = inputSeguro("Fecha inicio (YYYY-MM-DD): ")
    fin = inputSeguro("Fecha fin (YYYY-MM-DD): ")
    
    if validarFecha(inicio) and validarFecha(fin):
        lista = filtrarRangoFechas(gastos, inicio, fin)
        mostrarTabla(lista)
    else:
        print("Fechas inválidas.")
        pausarPantalla()

def mostrarTabla(lista):
    limpiarPantalla()
    if not lista:
        print("\n No hay registros para mostrar.")
        return pausarPantalla()

    tabla = [
        [g["id"], g["fecha"], g["categoria"].capitalize(), 
         f"${g['cantidad']:.2f}", g["descripcion"]]
        for g in lista
    ]

    print("\n" + tabulate(tabla, 
                          headers=["ID", "Fecha", "Categoría", "Monto", "Descripción"],
                          tablefmt="grid"))
    
    pausarPantalla()