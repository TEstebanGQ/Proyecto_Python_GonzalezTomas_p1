from datetime import datetime, timedelta
from collections import defaultdict

def totalDiario(gastos):
    hoy = datetime.now().strftime("%Y-%m-%d")
    return sum(g["cantidad"] for g in gastos if g["fecha"] == hoy)

def totalSemanal(gastos):
    hoy = datetime.now()
    hace7 = (hoy - timedelta(days=7)).replace(hour=0, minute=0, second=0, microsecond=0)
    return sum(
        g["cantidad"]
        for g in gastos
        if hace7 <= datetime.strptime(g["fecha"], "%Y-%m-%d") <= hoy
    )

def totalMensual(gastos):
    hoy = datetime.now()
    return sum(
        g["cantidad"]
        for g in gastos
        if datetime.strptime(g["fecha"], "%Y-%m-%d").month == hoy.month
        and datetime.strptime(g["fecha"], "%Y-%m-%d").year == hoy.year
    )

def generarReporteDiario(gastos):
    hoy = datetime.now().strftime("%Y-%m-%d")
    gastos_hoy = [g for g in gastos if g["fecha"] == hoy]
    
    return {
        "periodo": "Diario",
        "fecha": hoy,
        "gastos": gastos_hoy,
        "total": totalDiario(gastos),
        "por_categoria": agruparPorCategoria(gastos_hoy)
    }

def generarReporteSemanal(gastos):
    hoy = datetime.now()
    hace7 = (hoy - timedelta(days=7)).replace(hour=0, minute=0, second=0, microsecond=0)
    
    gastos_semana = [
        g for g in gastos
        if hace7 <= datetime.strptime(g["fecha"], "%Y-%m-%d") <= hoy
    ]
    
    return {
        "periodo": "Semanal",
        "fecha_inicio": hace7.strftime("%Y-%m-%d"),
        "fecha_fin": hoy.strftime("%Y-%m-%d"),
        "gastos": gastos_semana,
        "total": totalSemanal(gastos),
        "por_categoria": agruparPorCategoria(gastos_semana)
    }

def generarReporteMensual(gastos):
    hoy = datetime.now()
    
    gastos_mes = [
        g for g in gastos
        if datetime.strptime(g["fecha"], "%Y-%m-%d").month == hoy.month
        and datetime.strptime(g["fecha"], "%Y-%m-%d").year == hoy.year
    ]
    
    return {
        "periodo": "Mensual",
        "mes": hoy.strftime("%B %Y"),
        "gastos": gastos_mes,
        "total": totalMensual(gastos),
        "por_categoria": agruparPorCategoria(gastos_mes)
    }

def agruparPorCategoria(gastos):
    categorias = defaultdict(float)
    for gasto in gastos:
        categorias[gasto["categoria"]] += gasto["cantidad"]
    return dict(categorias)