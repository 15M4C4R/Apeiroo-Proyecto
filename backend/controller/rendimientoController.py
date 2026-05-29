import datetime
from flask import jsonify
from db.rendimientoDB import *
from utils.condiciones_alerta import comprobar_alertas

def procesar_rendimiento(data):
    
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
    
    insertar_rendimiento(documento)
    
    comprobar_alertas(documento)
    
    return jsonify({"mensaje": "Datos recibidos correctamente"}), 200

def obtener_rendimiento_actual(vm_id):
    
    rendimiento = buscar_rendimiento_por_id(vm_id)
    
    if not rendimiento:
        return jsonify({"error": "No se han encontrado datos para la maquina virtual"}), 404
    
    return jsonify(rendimiento), 200

def obtener_rendimiento_historico(vm_id):
    
    rendimiento = buscar_rendimiento_historico_por_id(vm_id)
    
    if not rendimiento:
        return jsonify({"error": "No se han encontrado datos para la maquina virtual"}), 404
    
    return jsonify(rendimiento), 200