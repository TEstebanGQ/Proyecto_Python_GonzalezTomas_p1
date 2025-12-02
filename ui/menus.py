from utils.screenControllers import limpiarPantalla, pausarPantalla
from core.gastoManager import registrar_gasto, listar_gastos
from core.calculos import total_diario, total_semanal, total_mensual, totales_por_categoria
from core.reportes import reporte_diario, reporte_semanal, reporte_mensual, guardar_reporte_json
from utils.formatting import mostrar_tabla_gastos, print_key_values, print_success, print_error


def menu_principal():
    while True:
        limpiarPantalla()
        print("""
=============================================
         Simulador de Gasto Diario
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Salir
=============================================
""")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_registro()
        elif opcion == "2":
            menu_listar()
        elif opcion == "3":
            menu_calculos()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            confirmar_salida()
        else:
            print("Opción inválida. Intente de nuevo.")
            pausarPantalla()


def confirmar_salida():
    """Confirma si el usuario desea salir del programa"""
    while True:
        respuesta = input("\n¿Desea salir del programa? (S/N): ").strip().upper()
        if respuesta == 'S':
            print("Saliendo del programa...")
            pausarPantalla()
            exit()
        elif respuesta == 'N':
            return
        else:
            print("Opción inválida. Ingrese 'S' para Sí o 'N' para No.")


# --- MENÚ REGISTRO -------------------------

def menu_registro():
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
        while True:
            confirmar = input("\nIngrese 'S' para guardar o 'C' para cancelar: ").strip().upper()
            if confirmar == 'S':
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
                break
            elif confirmar == 'C':
                print("\nRegistro cancelado.")
                break
            else:
                print("Opción inválida. Ingrese 'S' o 'C'.")
            
    except ValueError as e:
        print("\n" + "="*45)
        print_error(str(e))
        print("="*45)
    except Exception as e:
        print("\n" + "="*45)
        print_error(f"Error al registrar el gasto: {str(e)}")
        print("="*45)
    
    pausarPantalla()



def menu_listar():
    while True:
        limpiarPantalla()
        print("""
=============================================
                Listar Gastos
=============================================
Seleccione una opción para filtrar los gastos:

1. Ver todos los gastos
2. Filtrar por categoría
3. Filtrar por rango de fechas
4. Regresar al menú principal
=============================================
""")
        opcion = input("Opción: ").strip()
        
        try:
            if opcion == "1":
                # Ver todos los gastos
                limpiarPantalla()
                print("=== Todos los Gastos ===\n")
                gastos = listar_gastos()
                
                if not gastos:
                    print("No hay gastos registrados aún.")
                else:
                    print(f"Total de gastos registrados: {len(gastos)}\n")
                    mostrar_tabla_gastos(gastos)
                    
                pausarPantalla()
                
            elif opcion == "2":
                # Filtrar por categoría
                limpiarPantalla()
                print("=== Filtrar por Categoría ===\n")
                print("Categorías disponibles:")
                print("1. Comida")
                print("2. Transporte")
                print("3. Entretenimiento")
                print("4. Otros\n")
                
                cat_opcion = input("Seleccione una categoría: ").strip()
                categorias_map = {
                    "1": "comida",
                    "2": "transporte",
                    "3": "entretenimiento",
                    "4": "otros"
                }
                
                if cat_opcion in categorias_map:
                    categoria_filtro = categorias_map[cat_opcion]
                    gastos = listar_gastos(lambda g: g['categoria'] == categoria_filtro)
                    
                    limpiarPantalla()
                    print(f"=== Gastos en categoría: {categoria_filtro.upper()} ===\n")
                    
                    if not gastos:
                        print(f"No hay gastos en la categoría '{categoria_filtro}'.")
                    else:
                        print(f"Total de gastos encontrados: {len(gastos)}\n")
                        mostrar_tabla_gastos(gastos)
                else:
                    print("Opción inválida.")
                    
                pausarPantalla()
                
            elif opcion == "3":
                # Filtrar por rango de fechas
                limpiarPantalla()
                print("=== Filtrar por Rango de Fechas ===\n")
                print("Ingrese las fechas en formato: YYYY-MM-DD")
                fecha_inicio = input("Fecha de inicio: ").strip()
                fecha_fin = input("Fecha de fin: ").strip()
                
                try:
                    from datetime import datetime
                    inicio = datetime.fromisoformat(fecha_inicio)
                    fin = datetime.fromisoformat(fecha_fin)
                    
                    # Ajustar fin al final del día
                    fin = fin.replace(hour=23, minute=59, second=59)
                    
                    gastos = listar_gastos(
                        lambda g: inicio <= datetime.fromisoformat(g['fecha'].split('.')[0]) <= fin
                    )
                    
                    limpiarPantalla()
                    print(f"=== Gastos del {fecha_inicio} al {fecha_fin} ===\n")
                    
                    if not gastos:
                        print("No hay gastos en el rango de fechas especificado.")
                    else:
                        print(f"Total de gastos encontrados: {len(gastos)}\n")
                        mostrar_tabla_gastos(gastos)
                        
                        # Mostrar total
                        total = sum(g['monto'] for g in gastos)
                        print(f"\nTotal en el período: ${total:.2f}")
                        
                except ValueError:
                    print_error("Formato de fecha inválido. Use YYYY-MM-DD")
                    
                pausarPantalla()
                
            elif opcion == "4":
                return
            else:
                print("Opción inválida.")
                pausarPantalla()
                
        except Exception as e:
            print_error(f"Error al listar gastos: {str(e)}")
            pausarPantalla()


# --- MENÚ CÁLCULOS -------------------------

def menu_calculos():
    while True:
        limpiarPantalla()
        print("""
=============================================
          Calcular Total de Gastos
=============================================
Seleccione el periodo de cálculo:

1. Calcular total diario
2. Calcular total semanal
3. Calcular total mensual
4. Regresar al menú principal
=============================================
""")
        opcion = input("Opción: ").strip()

        try:
            if opcion == "1":
                limpiarPantalla()
                print("""
=============================================
              Total Diario
=============================================
""")
                total = total_diario()
                print(f"Total gastado hoy: ${total:.2f}\n")
                
                # Mostrar por categoría
                print("Desglose por categoría:")
                categorias = totales_por_categoria()
                if categorias:
                    for cat, monto in categorias.items():
                        porcentaje = (monto / total * 100) if total > 0 else 0
                        print(f"  • {cat.capitalize()}: ${monto:.2f} ({porcentaje:.1f}%)")
                else:
                    print("  No hay gastos registrados hoy.")
                print("="*45)
                    
            elif opcion == "2":
                limpiarPantalla()
                print("""
=============================================
              Total Semanal
=============================================
""")
                total = total_semanal()
                print(f"Total gastado en los últimos 7 días: ${total:.2f}\n")
                
                # Mostrar por categoría
                print("Desglose por categoría:")
                categorias = totales_por_categoria()
                if categorias:
                    for cat, monto in categorias.items():
                        porcentaje = (monto / total * 100) if total > 0 else 0
                        print(f"  • {cat.capitalize()}: ${monto:.2f} ({porcentaje:.1f}%)")
                else:
                    print("  No hay gastos registrados en la última semana.")
                print("="*45)
                    
            elif opcion == "3":
                limpiarPantalla()
                print("""
=============================================
              Total Mensual
=============================================
""")
                total = total_mensual()
                print(f"Total gastado este mes: ${total:.2f}\n")
                
                # Mostrar por categoría
                print("Desglose por categoría:")
                categorias = totales_por_categoria()
                if categorias:
                    for cat, monto in categorias.items():
                        porcentaje = (monto / total * 100) if total > 0 else 0
                        print(f"  • {cat.capitalize()}: ${monto:.2f} ({porcentaje:.1f}%)")
                else:
                    print("  No hay gastos registrados este mes.")
                print("="*45)
                    
            elif opcion == "4":
                return
            else:
                print("Opción inválida.")
                
        except Exception as e:
            print_error(f"Error al calcular totales: {str(e)}")

        pausarPantalla()


# --- MENÚ REPORTES --------------------------

def menu_reportes():
    while True:
        limpiarPantalla()
        print("""
=============================================
           Generar Reporte de Gastos
=============================================
Seleccione el tipo de reporte:

1. Reporte diario
2. Reporte semanal
3. Reporte mensual
4. Regresar al menú principal
=============================================
""")
        opcion = input("Opción: ").strip()

        if opcion in ["1", "2", "3"]:
            submenu_reporte(opcion)
        elif opcion == "4":
            return
        else:
            print("Opción inválida.")
            pausarPantalla()


def submenu_reporte(tipo_opcion):
    """Submenú para mostrar o guardar el reporte"""
    
    # Generar el reporte según la opción
    try:
        if tipo_opcion == "1":
            reporte = reporte_diario()
            nombre_tipo = "Diario"
            nombre_archivo = "reporte_diario"
        elif tipo_opcion == "2":
            reporte = reporte_semanal()
            nombre_tipo = "Semanal"
            nombre_archivo = "reporte_semanal"
        elif tipo_opcion == "3":
            reporte = reporte_mensual()
            nombre_tipo = "Mensual"
            nombre_archivo = "reporte_mensual"
        else:
            return
        
        while True:
            limpiarPantalla()
            print(f"""
=============================================
         Reporte {nombre_tipo}
=============================================
Después de seleccionar el tipo de reporte, 
se ofrece la opción de ver el reporte en 
pantalla o guardar el reporte en un archivo JSON.

1. Mostrar en pantalla
2. Guardar como JSON
3. Regresar
=============================================
""")
            sub_opcion = input("Opción: ").strip()
            
            if sub_opcion == "1":
                # Mostrar en pantalla
                limpiarPantalla()
                print(f"""
=============================================
         Reporte {nombre_tipo} - Pantalla
=============================================
""")
                print(f"Total: ${reporte['total']:.2f}\n")
                
                if reporte['por_categoria']:
                    print("Desglose por categoría:")
                    for cat, monto in reporte['por_categoria'].items():
                        porcentaje = (monto / reporte['total'] * 100) if reporte['total'] > 0 else 0
                        print(f"  • {cat.capitalize()}: ${monto:.2f} ({porcentaje:.1f}%)")
                else:
                    print("No hay gastos en este período.")
                
                print("="*45)
                pausarPantalla()
                
            elif sub_opcion == "2":
                # Guardar como JSON
                limpiarPantalla()
                print(f"""
=============================================
         Guardar Reporte {nombre_tipo}
=============================================
""")
                
                ruta = guardar_reporte_json(reporte, nombre_archivo)
                print_success("¡Reporte guardado exitosamente!")
                print(f"\nUbicación: {ruta}")
                print("="*45)
                
                pausarPantalla()
                
            elif sub_opcion == "3":
                return
            else:
                print("Opción inválida.")
                pausarPantalla()
                
    except Exception as e:
        print_error(f"Error al generar el reporte: {str(e)}")
        pausarPantalla()