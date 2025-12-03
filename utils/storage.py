import json
from pathlib import Path

_data_cache = None
DATA_FILE = Path('data/gastos.json')
REPORTS_DIR = Path('data/reports')

def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text('[]', encoding='utf-8')
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def load_data(use_cache=True):
    global _data_cache
    if use_cache and _data_cache is not None:
        return _data_cache
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            _data_cache = json.load(f)
        return _data_cache
    except json.JSONDecodeError:
        _data_cache = []
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        return _data_cache
    except FileNotFoundError:
        ensure_data_file()
        _data_cache = []
        return _data_cache

def save_data(data):
    global _data_cache
    _data_cache = data
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_report(reporte, nombre_archivo='reporte'):
    import datetime
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    nombre = f"{nombre_archivo}_{ts}.json"
    ruta = REPORTS_DIR / nombre
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(reporte, f, ensure_ascii=False, indent=2)
    return str(ruta)