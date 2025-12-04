from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.formatting import print_success, print_error
from core.gastoManager import registrar_gasto
from core.validators import obtener_categorias_usadas
from ui.menuSystem import mostrar_confirmacion


def seleccionar_categoria():
    limpiarPantalla()
    categorias_existentes = obtener_categorias_usadas()
    
    print("\n--- Seleccionar Categoría ---")
    
    if categorias_existentes:

        print("\nCategorías disponibles:")
        for i, cat in enumerate(categorias_existentes, 1):
            print(f"  {i}. {cat.capitalize()}")
        print(f"  {len(categorias_existentes) + 1}. Crear nueva categoría")
        interfaz
        while True:
            opcion = input("\nSeleccione una opción: ").strip()
            
            try:
                opcion_num = int(opcion)
        
                if 1 <= opcion_num <= len(categorias_existentes):
                    return categorias_existentes[opcion_num - 1]
                
                elif opcion_num == len(categorias_existentes) + 1:
                    nueva_cat = input("\nIngrese el nombre de la nueva categoría: ").strip().lower()
                    if nueva_cat:
                        return nueva_cat
                    else:
                        print("El nombre de la categoría no puede estar vacío.")
                else:
                    print("Opción inválida. Intente de nuevo.")
                    return
            
            except ValueError:
                print("Por favor ingrese un número válunaido.")
    else:
        limpiarPantalla()
        print("\nNo hay categorías registradas aún, rdegistre .")
        nueva_cat = input("Ingrese el nombre de la nueva categoría: ").strip().lower()
        if nueva_cat:
            return nueva_cat
        return None


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
        monto_str = input("- Monto del gasto: $").strip()
        
        categoria_str = seleccionar_categoria()
        
        if not categoria_str:
            print("\n" + "="*45)
            print_error("Debe ingresar una categoría válida.")
            print("="*45)
            pausarPantalla()
            return
 
        descripcion = input("\n- Descripción (opcional): ").strip()
        if mostrar_confirmacion("¿Desea guardar este gasto?"):
            gasto = registrar_gasto(monto_str, categoria_str, descripcion)
            
            print("\n" + "-"*45)
            print_success("¡Gasto registrado exitosamente!")
            print(f"  ID: {gasto['id']}")
            print(f"  Monto: ${gasto['monto']:.2f}")
            print(f"  Categoría: {gasto['categoria'].capitalize()}")
            print(f"  Fecha: {gasto['fecha']}")
            if gasto['descripcion']:
                print(f"  Descripción: {gasto['descripcion']}")
            print("-"*45)
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