import re
from difflib import get_close_matches
from data.storage import load_data

def obtener_categorias_usadas():
    """Obtiene todas las categorías únicas que han sido usadas"""
    gastos = load_data()
    categorias = set()
    for gasto in gastos:
        if 'categoria' in gasto and gasto['categoria']:
            categorias.add(gasto['categoria'].lower().strip())
    return sorted(list(categorias))


def validar_monto(text):
    if not isinstance(text, str):
        return None
    s = text.strip().replace(',', '.')
    if s == '':
        return None
    # permitir números positivos
    try:
        val = float(s)
        if val <= 0:
            return None
        # redondear a 2 decimales
        return round(val, 2)
    except Exception:
        return None


def corregir_categoria(cat):
    """Valida y corrige la categoría ingresada"""
    if not isinstance(cat, str):
        return None
    
    c = cat.lower().strip()
    
    if not c:
        return None
    
    # Validar que solo contenga letras, números y espacios
    if not re.match(r'^[a-záéíóúñ0-9\s]+$', c, re.IGNORECASE):
        return None
    
    # Obtener categorías existentes
    categorias_existentes = obtener_categorias_usadas()
    
    # Si la categoría ya existe, retornarla
    if c in categorias_existentes:
        return c
    
    # Buscar sugerencias similares
    sugerencias = get_close_matches(c, categorias_existentes, n=1, cutoff=0.7)
    
    if sugerencias:
        # Si hay una sugerencia muy similar, usar la existente
        return sugerencias[0]
    
    # Si no hay coincidencias, es una categoría nueva válida
    return c


def validar_fecha_iso(fecha_str):
    # formato ISO esperado: 2025-12-02T12:34:56
    import datetime
    try:
        datetime.datetime.fromisoformat(fecha_str)
        return True
    except Exception:
        return False