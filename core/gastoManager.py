from ui.prompts import inputSeguro, confirmarAccion
from utils.validators import validarFecha, validarCantidad
from utils.screenControllers import pausarPantalla, limpiarPantalla
from core.storage import *

def seleccionarCategoria(data):
    limpiarPantalla()
    print("""
=============================================
         Seleccionar Categoría
=============================================
""")
    
    categorias = data["categorias"]
    
    if categorias:
        print("\nCategorías disponibles:")
        for idx, cat in enumerate(categorias, start=1):
            print(f"  {idx}. {cat.capitalize()}")
        print(f"  {len(categorias) + 1}. Crear nueva categoría")
        
        while True:
            opcion = inputSeguro("\nSeleccione una opción: ")
            if not opcion:
                return None
            
            try:
                opcionNum = int(opcion)
                
                if 1 <= opcionNum <= len(categorias):
                    return categorias[opcionNum - 1]
                
                elif opcionNum == len(categorias) + 1:
                    nuevaCat = inputSeguro("\nIngrese el nombre de la nueva categoría: ")
                    if nuevaCat:
                        nuevaCat = nuevaCat.lower()
                        if nuevaCat not in categorias:
                            data["categorias"].append(nuevaCat)
                            print(f" Nueva categoría '{nuevaCat}' creada.")
                        return nuevaCat
                    else:
                        print(" El nombre de la categoría no puede estar vacío.")
                        return None
                else:
                    print(" Opción inválida. Intente de nuevo.")
            
            except ValueError:
                print(" Por favor ingrese un número válido.")
    else:
        print("\n No hay categorías registradas aún.")
        nuevaCat = inputSeguro("Ingrese el nombre de la nueva categoría: ")
        if nuevaCat:
            nuevaCat = nuevaCat.lower()
            data["categorias"].append(nuevaCat)
            return nuevaCat
        return None

def registrarGasto():
    while True:
        limpiarPantalla()
        print("""
=============================================
            Registrar Nuevo Gasto
=============================================
""")

        data = loadData()
        while True:
            fecha = inputSeguro("Fecha (YYYY-MM-DD): ")
            if not fecha:
                print(" Operación cancelada.")
                pausarPantalla()
                return
            if validarFecha(fecha):
                break

        while True:
            cantidad = inputSeguro("Monto: ")
            if not cantidad:
                print(" Operación cancelada.")
                pausarPantalla()
                return
            if validarCantidad(cantidad):
                break

        categoria = seleccionarCategoria(data)
        if not categoria:
            print(" Categoría inválida.")
            pausarPantalla()
            continue

        descripcion = inputSeguro("Descripción (opcional): ")
        if descripcion is None:
            descripcion = ""

        if not confirmarAccion("¿Guardar gasto? (S/N): "):
            print(" Operación cancelada.")
            pausarPantalla()
            continue

        gastoId = nextId(data)

        gasto = {
            "id": gastoId,
            "fecha": fecha,
            "categoria": categoria,
            "cantidad": float(cantidad),
            "descripcion": descripcion
        }

        data["gastos"].append(gasto)
        saveData(data)

        print(" Gasto registrado correctamente.")
        if not confirmarAccion("\n¿Desea registrar otro gasto? (S/N): "):
            break
        
    pausarPantalla()