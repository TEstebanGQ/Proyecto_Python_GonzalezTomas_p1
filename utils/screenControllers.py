import os
import sys

def pausarPantalla():
    try:
        if sys.platform.startswith('linux') or sys.platform == 'darwin':
            input('\nPresiona Enter para continuar .....')
        else:
            os.system('pause')
    except Exception:
        pass


def limpiarPantalla():
    try:
        if sys.platform.startswith('linux') or sys.platform == 'darwin':
            os.system('clear')
        else:
            os.system('cls')
    except Exception:
        pass