from db.configuracionDB import *
from flask import jsonify

def obtener_configuracion():
    configuracion = buscar_configuracion()
    
    if not configuracion:
        configuracion = {
            "_id": "global",
            "umbral_cpu": 80,
            "umbral_ram": 80,
            "umbral_almacenamiento": 80,
            "minutos_tolerancia": 5,
            "correo_destino": "becarios@apeiroo.com"
        }
        insertar_configuracion(configuracion)
    
    return configuracion, 200

def guardar_configuracion(configuracion):
    
    configuracion = actualizar_configuracion(configuracion)
    
    if not configuracion:
        return jsonify({"error": "No se ha podido actualizar la configuracion"}), 500
     
    return jsonify({"mensaje": "Configuracion actualizada correctamente"}), 200