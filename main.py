from ui.menus import menu_principal
from utils.storage import ensure_data_file
from utils.screenControllers import limpiarPantalla

def main():
    ensure_data_file()
    try:
        while True:
            limpiarPantalla()
            menu_principal()
    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))
        print("Reiniciando el menú principal...")
        main()

if __name__ == '__main__':
    main()