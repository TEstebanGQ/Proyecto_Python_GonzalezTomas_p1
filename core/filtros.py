from datetime import datetime

def filtrarCategoria(gastos, categoria):
    return [g for g in gastos if g["categoria"].lower() == categoria.lower()]

def filtrarRangoFechas(gastos, inicio, fin):
    inicioDt = datetime.strptime(inicio, "%Y-%m-%d")
    finDt = datetime.strptime(fin, "%Y-%m-%d")

    return [
        g for g in gastos
        if inicioDt <= datetime.strptime(g["fecha"], "%Y-%m-%d") <= finDt
    ]
