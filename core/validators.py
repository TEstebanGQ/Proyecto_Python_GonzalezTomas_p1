import re
from difflib import get_close_matches

CATEGORIAS = ['comida', 'transporte', 'entretenimiento', 'otros']


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
    if not isinstance(cat, str):
        return None
    c = cat.lower().strip()
    if c in CATEGORIAS:
        return c
    sugerencias = get_close_matches(c, CATEGORIAS, n=1, cutoff=0.5)
    return sugerencias[0] if sugerencias else None


def validar_fecha_iso(fecha_str):
    # formato ISO esperado: 2025-12-02T12:34:56
    import datetime
    try:
        datetime.datetime.fromisoformat(fecha_str)
        return True
    except Exception:
        return False
