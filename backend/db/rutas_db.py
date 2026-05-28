import datetime
from flask import Blueprint, jsonify, request
from db.db import get_db

rendimiento_bp = Blueprint('rendimiento', __name__)

@rendimiento_bp.route('/api/rendimiento/', methods=['POST'])
def guardar_rendimiento():
    db = get_db()
    data = request.json
    
    if not data:
        return jsonify({"error": "No se han proporcionado datos"}), 400
    
    documento = {
        "vm_id": data.get("vm_id"),
        "timestamp": datetime.datetime.now(datetime.timezone.utc),
        "cpu_uso": data.get("cpu_uso"),
        "ram_uso": data.get("ram_uso"),
        "almacenamiento_uso": data.get("almacenamiento_uso"),
        "procesos": data.get("procesos")
    }
    
    db["rendimiento"].insert_one(documento)
    return jsonify({"mensaje": "Datos recibidos correctamente"}), 200

@rendimiento_bp.route('/api/rendimiento/<nombre_vm>/actual', methods=['GET'])
def obtener_rendimiento_actual(nombre_vm):
    db = get_db()
    rendimiento = db["rendimiento"].find_one({"vm_id": nombre_vm}, {"_id": 0}, sort=[("timestamp", -1)])
    
    if not rendimiento:
        return jsonify({"error": "No se han encontrado datos para la maquina virtual"}), 404
    
    return jsonify(rendimiento), 200

@rendimiento_bp.route('/api/rendimiento/<nombre_vm>/historico', methods=['GET'])
def obtener_rendimiento_historico(nombre_vm):
    db = get_db()
    rendimiento = list(db["rendimiento"].find({"vm_id": nombre_vm}, {"_id":0}).sort("timestamp", -1).limit(50))
    return jsonify(rendimiento), 200