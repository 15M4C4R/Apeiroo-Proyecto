from flask import Blueprint, request
from utils.ssh import Ssh
from controller.comandoController import *

comando_bp = Blueprint('comando', __name__)

@comando_bp.route('/api/ejecutar-comando/', methods=['POST'])
def recibir_comando():
    
    data = request.json
    
    return ejecutar_comando(data)