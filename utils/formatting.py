from datetime import datetime

try:
    from tabulate import tabulate
    TABULATE_DISPONIBLE = True
except ImportError:
    TABULATE_DISPONIBLE = False

def formatear_fecha(fecha_iso):
    try:
        fecha = datetime.fromisoformat(fecha_iso.split('.')[0])
        return fecha.strftime('%Y-%m-%d %H:%M')
    except (ValueError, AttributeError):
        return fecha_iso

def formatear_monto(monto):
    return f"${monto:,.2f}"

def truncar_texto(texto, longitud_maxima=30):
    if not texto:
        return ''
    
    if len(texto) <= longitud_maxima:
        return texto
    
    return texto[:longitud_maxima - 3] + '...'


def mostrar_tabla_gastos(gastos):

    if not gastos:
        print('No hay gastos para mostrar.')
        return

    filas = []
    for gasto in gastos:
        fila = [
            str(gasto.get('id', ''))[:8] + '...',  # ID truncado
            formatear_fecha(gasto.get('fecha', '')),
            gasto.get('categoria', '').capitalize(),
            formatear_monto(gasto.get('monto', 0)),
            truncar_texto(gasto.get('descripcion', ''), 40)
        ]
        filas.append(fila)
    
    headers = ['ID', 'Fecha', 'Categoría', 'Monto', 'Descripción']
    
    if TABULATE_DISPONIBLE:
        print(tabulate(filas, headers=headers, tablefmt='simple'))
    else:
        _mostrar_tabla_simple(headers, filas)


def _mostrar_tabla_simple(headers, filas):
    anchos = [len(h) for h in headers]
    
    for fila in filas:
        for i, valor in enumerate(fila):
            anchos[i] = max(anchos[i], len(str(valor)))
    
    # Imprimir encabezados
    linea_header = ' | '.join(
        h.ljust(anchos[i]) for i, h in enumerate(headers)
    )
    print(linea_header)
    print('-' * len(linea_header))
    
    # Imprimir filas
    for fila in filas:
        linea = ' | '.join(
            str(valor).ljust(anchos[i]) for i, valor in enumerate(fila)
        )
        print(linea)

def print_key_values(diccionario):
    if not diccionario:
        print('Sin datos')
        return
    
    for clave, valor in diccionario.items():
        print(f"- {clave}: {valor}")

def print_success(mensaje):
    print(f" [OK] {mensaje}")

def print_error(mensaje):
    print(f" [ERROR] {mensaje}")

def print_warning(mensaje):
    print(f" [ADVERTENCIA] {mensaje}")

def print_info(mensaje):
    print(f" [INFO] {mensaje}")

def crear_separador(caracter='=', longitud=45):
    return caracter * longitud

def centrar_texto(texto, longitud=45):
    return texto.center(longitud)