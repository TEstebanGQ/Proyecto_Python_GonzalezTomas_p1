from datetime import datetime, timedelta


def ahora_iso():
    return datetime.now().isoformat()

def iso_a_fecha(iso):
    try:
        return datetime.fromisoformat(iso)
    except ValueError:
        raise ValueError(f"Formato ISO inválido: {iso}")


def fecha_hoy():
    return datetime.now().date()


def hace_dias(n):
    return datetime.now() - timedelta(days=n)


def parse_fecha_range(text):
    try:
        parts = text.split('a')
        if len(parts) != 2:
            return None, None
        inicio = parts[0].strip()
        fin = parts[1].strip()
        return inicio, fin
    except Exception:
        return None, None