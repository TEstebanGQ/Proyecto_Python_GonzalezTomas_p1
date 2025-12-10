from datetime import datetime, timedelta
import json

def calcularPromedioHistorico(gastos, diasHistoricos=30):
    hoy = datetime.now()
    fechaInicio = hoy - timedelta(days=diasHistoricos)
    gastosPeriodo = []
    for gasto in gastos:
        fechaGasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d")
        if fechaInicio <= fechaGasto <= hoy:
            gastosPeriodo.append(gasto)
    
    if not gastosPeriodo:
        return None, None, 0
    
    totalPeriodo = 0
    for gasto in gastosPeriodo:
        totalPeriodo += gasto["cantidad"]
    
    categoriasTotal = {}
    for gasto in gastosPeriodo:
        categoria = gasto["categoria"]
        if categoria in categoriasTotal:
            categoriasTotal[categoria] += gasto["cantidad"]
        else:
            categoriasTotal[categoria] = gasto["cantidad"]
    
    fechasUnicas = []
    for gasto in gastosPeriodo:
        if gasto["fecha"] not in fechasUnicas:
            fechasUnicas.append(gasto["fecha"])
    
    diasConGastos = len(fechasUnicas)
    if diasConGastos == 0:
        diasConGastos = 1
    
    promedioDiario = totalPeriodo / diasConGastos
    
    promedioPorCategoria = {}
    for categoria, total in categoriasTotal.items():
        promedioPorCategoria[categoria] = total / diasConGastos
    
    return promedioDiario, promedioPorCategoria, len(gastosPeriodo)

def generarProyeccion(gastos, diasFuturos):
    promedioDiario, promedioPorCategoria, numGastos = calcularPromedioHistorico(gastos)
    
    if promedioDiario is None:
        return {
            "error": "No hay datos históricos suficientes",
            "datosDisponibles": numGastos
        }
    
    proyeccionTotal = promedioDiario * diasFuturos
    
    proyeccionPorCategoria = {}
    for categoria, promedio in promedioPorCategoria.items():
        proyeccionPorCategoria[categoria] = promedio * diasFuturos
    
    categoriasOrdenadas = []
    for categoria, monto in proyeccionPorCategoria.items():
        categoriasOrdenadas.append({
            "categoria": categoria,
            "montoProyectado": round(monto, 2)
        })
    
    categoriasOrdenadas.sort(key=lambda x: x["montoProyectado"], reverse=True)
    
    return {
        "proyeccion": {
            "diasProyectados": diasFuturos,
            "gastoTotalProyectado": round(proyeccionTotal, 2),
            "gastoPorCategoria": {
                cat: round(monto, 2)
                for cat, monto in proyeccionPorCategoria.items()
            },
            "categoriasOrdenadas": categoriasOrdenadas,
            "datosHistoricosUsados": numGastos
        }
    }

def guardarProyeccion(proyeccion):
    timestamp = datetime.now().strftime("%Y%m%d")
    nombreArchivo = f"data/reporte_proyeccion_{timestamp}.json"
    
    try:
        with open(nombreArchivo, "w", encoding="utf-8") as f:
            json.dump(proyeccion, f, indent=4, ensure_ascii=False)
        return nombreArchivo
    except Exception as e:
        raise Exception(f"Error al guardar proyección: {e}")