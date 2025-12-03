from data.storage import load_data
from utils.dateUtils import iso_a_fecha, fecha_hoy, hace_dias
from datetime import datetime


def filtrar_gastos_por_periodo(gastos, filtro_func):
    return [g for g in gastos if filtro_func(g)]

def es_gasto_hoy(gasto):
    return iso_a_fecha(gasto['fecha']).date() == fecha_hoy()

def es_gasto_ultima_semana(gasto):
    return iso_a_fecha(gasto['fecha']) >= hace_dias(7)


def es_gasto_mes_actual(gasto):
    hoy = datetime.now()
    fecha_gasto = iso_a_fecha(gasto['fecha'])
    return fecha_gasto.year == hoy.year and fecha_gasto.month == hoy.month

def calcular_total(gastos):
    return sum(g['monto'] for g in gastos)

def total_diario():
    gastos = load_data()
    gastos_filtrados = filtrar_gastos_por_periodo(gastos, es_gasto_hoy)
    return calcular_total(gastos_filtrados)

def total_semanal():
    gastos = load_data()
    gastos_filtrados = filtrar_gastos_por_periodo(gastos, es_gasto_ultima_semana)
    return calcular_total(gastos_filtrados)

def total_mensual():
    gastos = load_data()
    gastos_filtrados = filtrar_gastos_por_periodo(gastos, es_gasto_mes_actual)
    return calcular_total(gastos_filtrados)

def totales_por_categoria(filtro_func=None):
    gastos = load_data()
    
    if filtro_func:
        gastos = filtrar_gastos_por_periodo(gastos, filtro_func)
    
    resumen = {}
    for gasto in gastos:
        categoria = gasto['categoria']
        resumen[categoria] = resumen.get(categoria, 0) + gasto['monto']
    
    return resumen

def obtener_estadisticas_periodo(filtro_func=None):
    gastos = load_data()
    
    if filtro_func:
        gastos = filtrar_gastos_por_periodo(gastos, filtro_func)
    
    total = calcular_total(gastos)
    por_categoria = {}
    
    for gasto in gastos:
        categoria = gasto['categoria']
        por_categoria[categoria] = por_categoria.get(categoria, 0) + gasto['monto']
    
    return {
        'total': total,
        'por_categoria': por_categoria,
        'cantidad_gastos': len(gastos)
    }