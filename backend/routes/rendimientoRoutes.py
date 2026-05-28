import datetime
from flask import Blueprint, jsonify, request
from db.db import get_db
from backend.controller.rendimientoController import obtener_rendimiento_actual, obtener_rendimiento_historico, procesar_rendimiento

rendimiento_bp = Blueprint('rendimiento', __name__)
db = get_db()

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