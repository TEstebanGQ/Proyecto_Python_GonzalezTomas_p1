from data.storage import load_data
from utils.dateUtils import iso_a_fecha, fecha_hoy, hace_dias


def total_diario():
    hoy = fecha_hoy()
    gastos = load_data()
    return sum(g['monto'] for g in gastos if iso_a_fecha(g['fecha']).date() == hoy)


def total_semanal():
    gastos = load_data()
    limite = hace_dias(7)
    return sum(g['monto'] for g in gastos if iso_a_fecha(g['fecha']) >= limite)


def total_mensual():
    from datetime import datetime
    hoy = datetime.now()
    gastos = load_data()
    return sum(g['monto'] for g in gastos if iso_a_fecha(g['fecha']).year == hoy.year and iso_a_fecha(g['fecha']).month == hoy.month)


def totales_por_categoria(period_filter=None):
    gastos = load_data()
    if period_filter:
        gastos = [g for g in gastos if period_filter(g)]
    resumen = {}
    for g in gastos:
        resumen[g['categoria']] = resumen.get(g['categoria'], 0) + g['monto']
    return resumen