from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.formatting import print_success, print_error
from core.gastoManager import registrar_gasto
from ui.menuSystem import mostrar_confirmacion


def vista_registro_gasto():
    """Vista para registrar un nuevo gasto"""
    limpiarPantalla()
    print("""
=============================================
            Registrar Nuevo Gasto
=============================================
Ingrese la información del gasto:
""")
    
    try:
        # Solicitar datos al usuario
        monto_str = input("- Monto del gasto: $").strip()
        categoria_str = input("- Categoría (ej. comida, transporte, entretenimiento, otros): ").strip()
        descripcion = input("- Descripción (opcional): ").strip()
        
        # Confirmar o cancelar
        if mostrar_confirmacion("Ingrese 'S' para guardar o 'C' para cancelar"):
            # Registrar el gasto
            gasto = registrar_gasto(monto_str, categoria_str, descripcion)
            
            print("\n" + "="*45)
            print_success("¡Gasto registrado exitosamente!")
            print(f"  ID: {gasto['id']}")
            print(f"  Monto: ${gasto['monto']:.2f}")
            print(f"  Categoría: {gasto['categoria']}")
            print(f"  Fecha: {gasto['fecha']}")
            if gasto['descripcion']:
                print(f"  Descripción: {gasto['descripcion']}")
            print("="*45)
        else:
            print("\nRegistro cancelado.")
            
    except ValueError as e:
        print("\n" + "="*45)
        print_error(str(e))
        print("="*45)
    except Exception as e:
        print("\n" + "="*45)
        print_error(f"Error al registrar el gasto: {str(e)}")
        print("="*45)
    
    pausarPantalla()