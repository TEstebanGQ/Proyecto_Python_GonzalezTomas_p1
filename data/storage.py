import json
from pathlib import Path

DATA_FILE = Path('data/gastos.json')
REPORTS_DIR = Path('data/reports')


def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text('[]', encoding='utf-8')
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        return []
    except FileNotFoundError:
        ensure_data_file()
        return []


def save_data(data):
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