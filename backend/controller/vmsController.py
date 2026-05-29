from utils.seguridad import * 
from db.vmsDB import *
from flask import jsonify
from utils.ssh import Ssh

ssh = Ssh()


def procesar_vm(data):
    
    if not data:
        return jsonify({"error": "No se han proporcionado datos"}), 400
    
    resultado_conexion = ssh.nueva_vm(data.get("vm_id"), data.get("vm_host"), data.get("vm_usuario"), data.get("vm_contraseña"), Ssh.ORIGEN)

    if not resultado_conexion.get("exito"):
        return jsonify({"error": resultado_conexion.get("mensaje")}), 500
    
    contraseña = cifrar_texto(data.get("vm_contraseña"))
    
    vm = {
        "_id": data.get("vm_id"),
        "nombre": data.get("vm_nombre"),
        "host": data.get("vm_host"),
        "usuario": data.get("vm_usuario"),
        "contraseña": contraseña
    }
    
    insertar_vm(vm)
    
    return jsonify({"mensaje": "Máquina virtual creada correctamente"}), 200

def buscar_vm(vm_id):
    
    vm = buscar_vm_por_id(vm_id)
    
    if not vm:
        return jsonify({"error": "No se ha encontrado la Máquina virtual"}), 404
    else:
        vm
    
    return jsonify(vm), 200