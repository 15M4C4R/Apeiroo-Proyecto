from flask import Flask, jsonify, request
from flask_cors import CORS
from ssh import Ssh
from db.rutas_db import rendimiento_bp


app = Flask(__name__)
CORS(app)

app.register_blueprint(rendimiento_bp)

@app.route('/api/ejecutar-comando/', methods=['POST'])
def ejecutar_comando():
    data = request.json
    
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
