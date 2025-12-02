from data.storage import load_data, save_data
from utils.dateUtils import ahora_iso
from core.validators import validar_monto, corregir_categoria

def registrar_gasto(monto_str, categoria_str, descripcion=''):
    monto = validar_monto(monto_str)
    if monto is None:
        raise ValueError('Monto inválido')
    categoria = corregir_categoria(categoria_str)
    if categoria is None:
        raise ValueError('Categoría inválida')

    gasto = {
        'id': generar_id(),
        'fecha': ahora_iso(),
        'monto': monto,
        'categoria': categoria,
        'descripcion': descripcion.strip()
    }

    data = load_data()
    data.append(gasto)
    save_data(data)
    return gasto


def generar_id():
    # Simple id incremental basado en timestamp
    import time
    return int(time.time() * 1000)


def listar_gastos(filtro=None):
    data = load_data()
    if filtro is None:
        return data
    # filtro puede ser una función
    return [g for g in data if filtro(g)]