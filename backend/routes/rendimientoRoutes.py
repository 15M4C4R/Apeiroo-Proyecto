from flask import Blueprint, request
from backend.controller.rendimientoController import *

rendimiento_bp = Blueprint('rendimiento', __name__)

@rendimiento_bp.route('/api/rendimiento/', methods=['POST'])
def recibir_rendimiento():
    
    data = request.json
    
    return procesar_rendimiento(data)

@rendimiento_bp.route('/api/rendimiento/<nombre_vm>/actual', methods=['GET'])
def enviar_rendimiento_actual(nombre_vm):

    return obtener_rendimiento_actual(nombre_vm)

@rendimiento_bp.route('/api/rendimiento/<nombre_vm>/historico', methods=['GET'])
def enviar_rendimiento_historico(nombre_vm):

    return obtener_rendimiento_historico(nombre_vm)