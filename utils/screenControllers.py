import os
import sys

def pausarPantalla():
    try:
        input('Presione ENTER para continuar...')
    except KeyboardInterrupt:
        print("\nOperación cancelada.")

def limpiarPantalla():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")
