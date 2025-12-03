import re
from datetime import datetime
from difflib import get_close_matches
from data.storage import load_data


# Constantes
PATRON_CATEGORIA = r'^[a-záéíóúñ0-9\s]+$'
SIMILITUD_MINIMA = 0.7
MAX_SUGERENCIAS = 1


def obtener_categorias_usadas():
    gastos = load_data()
    categorias = set()
    
    for gasto in gastos:
        if 'categoria' in gasto and gasto['categoria']:
            categoria_normalizada = gasto['categoria'].lower().strip()
            if categoria_normalizada:
                categorias.add(categoria_normalizada)
    
    return sorted(list(categorias))


def validar_monto(text):
    if not isinstance(text, str):
        return None
    
    # Normalizar el texto
    texto_limpio = text.strip().replace(',', '.')
    
    if not texto_limpio:
        return None
    
    try:
        valor = float(texto_limpio)
        
        # Validar que sea positivo
        if valor <= 0:
            return None
        
        # Redondear a 2 decimales
        return round(valor, 2)
    
    except (ValueError, OverflowError):
        return None


def es_categoria_valida(categoria):
    if not categoria:
        return False
    
    return bool(re.match(PATRON_CATEGORIA, categoria, re.IGNORECASE))


def normalizar_categoria(categoria):
    if not isinstance(categoria, str):
        return None
    
    categoria_limpia = categoria.lower().strip()
    
    # Eliminar espacios múltiples
    categoria_limpia = ' '.join(categoria_limpia.split())
    
    return categoria_limpia if categoria_limpia else None


def buscar_categoria_similar(categoria, categorias_existentes):
    if not categorias_existentes:
        return None
    
    sugerencias = get_close_matches(
        categoria,
        categorias_existentes,
        n=MAX_SUGERENCIAS,
        cutoff=SIMILITUD_MINIMA
    )
    
    return sugerencias[0] if sugerencias else None


def corregir_categoria(categoria_str):
    # Normalizar la categoría
    categoria = normalizar_categoria(categoria_str)
    
    if not categoria:
        return None
    
    # Validar formato
    if not es_categoria_valida(categoria):
        return None
    
    # Obtener categorías existentes
    categorias_existentes = obtener_categorias_usadas()
    
    # Si la categoría ya existe, retornarla
    if categoria in categorias_existentes:
        return categoria
    
    # Buscar categoría similar
    categoria_similar = buscar_categoria_similar(categoria, categorias_existentes)
    
    if categoria_similar:
        return categoria_similar
    
    # Si no hay coincidencias, es una categoría nueva válida
    return categoria


def validar_fecha_iso(fecha_str):
    if not isinstance(fecha_str, str):
        return False
    
    try:
        datetime.fromisoformat(fecha_str)
        return True
    except (ValueError, TypeError):
        return False


def validar_rango_fechas(fecha_inicio_str, fecha_fin_str):
    try:
        fecha_inicio = datetime.fromisoformat(fecha_inicio_str)
        fecha_fin = datetime.fromisoformat(fecha_fin_str)
        
        # Validar que la fecha de inicio sea anterior a la de fin
        if fecha_inicio > fecha_fin:
            return None, None
        
        return fecha_inicio, fecha_fin
    
    except (ValueError, TypeError):
        return None, None