import uuid
from utils.storage import load_data, save_data
from utils.dateUtils import ahora_iso
from core.validators import validar_monto, corregir_categoria


def generar_id():
    return str(uuid.uuid4())


def crear_gasto(monto, categoria, descripcion=''):
    return {
        'id': generar_id(),
        'fecha': ahora_iso(),
        'monto': monto,
        'categoria': categoria,
        'descripcion': descripcion.strip()
    }


def registrar_gasto(monto_str, categoria_str, descripcion=''):
    monto = validar_monto(monto_str)
    if monto is None:
        raise ValueError('Monto inválido. Debe ser un número positivo.')

    categoria = corregir_categoria(categoria_str)
    if categoria is None:
        raise ValueError('Categoría inválida. Debe contener solo letras, números y espacios.')
 
    gasto = crear_gasto(monto, categoria, descripcion)
    data = load_data()
    data.append(gasto)
    save_data(data)
    
    return gasto


def listar_gastos(filtro=None):
    data = load_data()
    
    if filtro is None:
        return data
    
    return [gasto for gasto in data if filtro(gasto)]

def buscar_gasto_por_id(gasto_id):
    gastos = load_data()
    
    for gasto in gastos:
        if str(gasto['id']) == str(gasto_id):
            return gasto
    
    return None

def contar_gastos(filtro=None):
    return len(listar_gastos(filtro))