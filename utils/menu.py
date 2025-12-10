def menu(titulo, opciones):
    """
    Muestra un menú genérico y retorna la opción seleccionada
        titulo: Título del menú
        opciones: Tupla o lista con las opciones del menú
        int: Número de la opción seleccionada (1 a n)
    """
    print("=============================================")
    print(f"        {titulo}")
    print("=============================================")
    
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    
    print("=============================================")
    
    while True:
        try:
            eleccion = int(input("\nSeleccione una opción: "))
            if eleccion not in range(1, len(opciones) + 1):
                print(" Opción inválida. Intente nuevamente.")
            else:
                return eleccion
        except ValueError:
            print(" Debe ingresar un número válido.")
        except (KeyboardInterrupt, EOFError):
            print("\n Operación cancelada.")
            return len(opciones)  