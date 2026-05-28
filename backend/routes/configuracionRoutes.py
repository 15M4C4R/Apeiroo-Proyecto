from flask import Blueprint, request
from controller.configuracionController import *

configuracion_bp = Blueprint('configuracion', __name__)

@configuracion_bp.route('/api/configuracion/', methods=['GET'])
def enviar_configuracion():
    
    return obtener_configuracion()

@configuracion_bp.route('/api/configuracion/', methods=["PUT"])
def recibir_configuracion():
    
    data = request.json
    
    return guardar_configuracion(data)