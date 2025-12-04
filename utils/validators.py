import re
from datetime import datetime

def validarFecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validarCantidad(cantidad_str):
    try:
        cantidad = float(cantidad_str)
        return cantidad > 0
    except:
        return False

def validarCategoria(categoria, categorias_validas):
    return categoria.lower() in categorias_validas

def validarOpcionNumerica(opcion, minimo, maximo):
    if not opcion.isdigit():
        return False
    opcion = int(opcion)
    return minimo <= opcion <= maximo
