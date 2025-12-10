from ui.prompts import confirmarAccion
from utils.screenControllers import limpiarPantalla, pausarPantalla
from utils.menu import menu
from core.storage import loadData
from core.reportes import (generarReporteDiario, generarReporteSemanal, generarReporteMensual)
from tabulate import tabulate
import json
from datetime import datetime

def generarReporteMenu():
    opciones = (
        "Reporte diario",
        "Reporte semanal",
        "Reporte mensual",
        "Regresar al menú principal"
    )
    
    while True:
        data = loadData()
        gastos = data["gastos"]

        limpiarPantalla()
        opcion = menu("Generar Reporte de Gastos", opciones)
        
        reporte = None
        
        match opcion:
            case 1:
                reporte = generarReporteDiario(gastos)
            case 2:
                reporte = generarReporteSemanal(gastos)
            case 3:
                reporte = generarReporteMensual(gastos)
            case 4:
                break

        if reporte:
            mostrarReporte(reporte)

def mostrarReporte(reporte):
    limpiarPantalla()
    print(f"""
=============================================
         Reporte {reporte['periodo']}
=============================================
""")
    
    mostrarEncabezadoReporte(reporte)
    mostrarGastosReporte(reporte)
    mostrarResumenCategoriasReporte(reporte)
    mostrarTotalReporte(reporte)
    
    if confirmarAccion("\n¿Desea guardar este reporte en un archivo JSON? (S/N): "):
        guardarReporte(reporte)
    
    pausarPantalla()

def mostrarEncabezadoReporte(reporte):
    if reporte["periodo"] == "Diario":
        print(f"Fecha: {reporte['fecha']}")
    elif reporte["periodo"] == "Semanal":
        print(f"Período: {reporte['fecha_inicio']} a {reporte['fecha_fin']}")
    else:
        print(f"Mes: {reporte['mes']}")

def mostrarGastosReporte(reporte):
    print("\n--- Gastos Registrados ---")
    
    if not reporte["gastos"]:
        print(" No hay gastos registrados en este período.")
    else:
        tabla = [
            [g["id"], g["fecha"], g["categoria"].capitalize(), 
             f"${g['cantidad']:.2f}", g["descripcion"]]
            for g in reporte["gastos"]
        ]
        print(tabulate(tabla, 
                      headers=["ID", "Fecha", "Categoría", "Monto", "Descripción"],
                      tablefmt="grid"))

def mostrarResumenCategoriasReporte(reporte):
    print("\n--- Resumen por Categoría ---")
    if reporte["por_categoria"]:
        tabla_cat = [
            [cat.capitalize(), f"${monto:.2f}"]
            for cat, monto in reporte["por_categoria"].items()
        ]
        print(tabulate(tabla_cat, 
                      headers=["Categoría", "Total"],
                      tablefmt="grid"))

def mostrarTotalReporte(reporte):
    print(f"\n✓ TOTAL {reporte['periodo'].upper()}: ${reporte['total']:.2f}")

def guardarReporte(reporte):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"data/reporte_{reporte['periodo'].lower()}_{timestamp}.json"
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(reporte, f, indent=4, ensure_ascii=False)
        print(f" Reporte guardado exitosamente en: {nombre_archivo}")
    except Exception as e:
        print(f" Error al guardar el reporte: {e}")