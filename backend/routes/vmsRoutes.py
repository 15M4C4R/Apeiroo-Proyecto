from flask import Blueprint, request
from controller.vmsController import *

vms_bp = Blueprint('vms', __name__)

@vms_bp.route('/api/vms', methods=['POST'])
def recibir_vm():
    data = request.json
    
    return procesar_vm(data)