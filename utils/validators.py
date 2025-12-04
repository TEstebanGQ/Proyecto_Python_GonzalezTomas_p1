import re
from datetime import datetime

def validarFecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        hoy = datetime.now()
        if fecha > hoy:
            print(" Error: La fecha no puede ser mayor a la fecha actual.")
            return False
        
        return True
    except ValueError:
        print(" Error: Formato de fecha inválido. Use YYYY-MM-DD.")
        return False

def validarCantidad(cantidad_str):
    try:
        cantidad = float(cantidad_str)
        if cantidad <= 0:
            print(" Error: La cantidad debe ser mayor a 0.")
            return False
        return True
    except:
        print(" Error: Cantidad inválida. Ingrese un número válido.")
        return False

def validarCategoria(categoria, categorias_validas):
    return categoria.lower() in categorias_validas

def validarOpcionNumerica(opcion, minimo, maximo):
    if not opcion.isdigit():
        return False
    opcion = int(opcion)
    return minimo <= opcion <= maximo