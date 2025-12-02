from ui.menus import menu_principal
from data.storage import ensure_data_file
from utils.screenControllers import limpiarPantalla

def main():
    # Asegura que el archivo de datos exista
    ensure_data_file()
    try:
        while True:
            limpiarPantalla()
            menu_principal()
    except Exception as e:
        # Nunca debe romper la consola; se podría loggear el error
        print("Ocurrió un error inesperado:", str(e))
        print("Reiniciando el menú principal...")
        main()

if __name__ == '__main__':
    main()