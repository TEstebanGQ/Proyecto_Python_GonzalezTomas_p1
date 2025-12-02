try:
    from tabulate import tabulate
except Exception:
    tabulate = None


def mostrar_tabla_gastos(gastos):
    if not gastos:
        print('No hay gastos para mostrar.')
        return
    rows = []
    for g in gastos:
        rows.append([g.get('id'), g.get('fecha'), g.get('categoria'), g.get('monto'), g.get('descripcion')])
    headers = ['ID','Fecha','Categoria','Monto','Descripcion']
    if tabulate:
        print(tabulate(rows, headers=headers))
    else:
        # fallback simple
        print(headers)
        for r in rows:
            print(r)


def print_key_values(d):
    if not d:
        print('Sin datos')
        return
    for k, v in d.items():
        print(f"- {k}: {v}")


def print_success(msg):
    print(f"[OK] {msg}")


def print_error(msg):
    print(f"[ERROR] {msg}")