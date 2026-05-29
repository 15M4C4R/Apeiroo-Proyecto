from flask import jsonify
from utils.ssh import Ssh

def ejecutar_comando(data):
    if not data:
        return jsonify({"error": "No se han proporcionado datos"}), 400
    
    host = data.get("host")
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")
    comando = data.get("comando")
    
    if not all ([host, usuario, contraseña, comando]):
        return jsonify({"error": "Todos los campos son obligatorios (host, usuario, contraseña o comando)"}), 400
    
    ssh = Ssh()
    resultado = ssh.ejecutar_atomico(host, usuario, contraseña, comando)
    if resultado["exito"]:
        return jsonify({
            "mensaje": "Comando ejecutado con exito",
            "salida_terminal": resultado["mensaje"]
        }), 200
    else:
        return jsonify({
            "error": resultado["mensaje"],
        }), 500