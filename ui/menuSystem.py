from utils.screenControllers import limpiarPantalla, pausarPantalla


class Menu:
    """Sistema de menú reutilizable"""
    
    def __init__(self, titulo, opciones):
        """
        titulo: str - Título del menú
        opciones: list[dict] - Lista de opciones con formato:
            [
                {'texto': 'Opción 1', 'accion': funcion1},
                {'texto': 'Opción 2', 'accion': funcion2},
                ...
            ]
        """
        self.titulo = titulo
        self.opciones = opciones
    
    def mostrar(self):
        """Muestra el menú y ejecuta la opción seleccionada"""
        while True:
            limpiarPantalla()
            self._imprimir_menu()
            
            opcion = input("Opción: ").strip()
            
            # Validar si la opción es válida
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(self.opciones):
                    accion = self.opciones[indice]['accion']
                    
                    # Si la acción retorna False, salir del menú
                    if accion and accion() == False:
                        break
                else:
                    print("Opción inválida. Intente de nuevo.")
                    pausarPantalla()
            except ValueError:
                print("Por favor ingrese un número válido.")
                pausarPantalla()
    
    def _imprimir_menu(self):
        """Imprime el menú en pantalla"""
        separador = "=" * 45
        print(f"\n{separador}")
        print(f"{self.titulo:^45}")
        print(separador)
        print("Seleccione una opción:\n")
        
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion['texto']}")
        
        print(separador)


def mostrar_confirmacion(mensaje):
    """
    Muestra un mensaje de confirmación S/N
    Retorna True si el usuario confirma, False en caso contrario
    """
    while True:
        respuesta = input(f"\n{mensaje} (S/N): ").strip().upper()
        if respuesta == 'S':
            return True
        elif respuesta == 'N':
            return False
        else:
            print("Opción inválida. Ingrese 'S' para Sí o 'N' para No.")


def mostrar_resultado(titulo, contenido, es_error=False):
    """
    Muestra un resultado formateado
    titulo: str - Título del resultado
    contenido: str o dict - Contenido a mostrar
    es_error: bool - Si es un mensaje de error
    """
    limpiarPantalla()
    separador = "=" * 45
    
    print(f"\n{separador}")
    print(f"{titulo:^45}")
    print(separador)
    
    if es_error:
        print(f"[ERROR] {contenido}")
    else:
        if isinstance(contenido, dict):
            for clave, valor in contenido.items():
                print(f"  {clave}: {valor}")
        else:
            print(contenido)
    
    print(separador)
    pausarPantalla()