from core.gastoManager import *

def inputSeguro(mensaje):
    try:
        valor = input(mensaje).strip()
        if valor == "":
            print("No puede dejar este campo vacío.")
            return None
        return valor
    except (KeyboardInterrupt, EOFError):
        print("\n Entrada cancelada por el usuario.")
        return None


def confirmarAccion(mensaje="¿Confirmar? (S/N): "):
    while True:
        try:
            respuesta = input(mensaje).strip().upper()
            
            if respuesta == "":
                print(" No puede dejar este campo vacío. Ingrese S para confirmar o N para cancelar.")
                continue
            
            if respuesta == "S":
                return True
            elif respuesta == "N":
                return False
            else:
                print(" Opción inválida. Ingrese 'S' para SÍ o 'N' para NO.")
                
        except (KeyboardInterrupt, EOFError):
            print("\n Entrada cancelada por el usuario.")
            return None