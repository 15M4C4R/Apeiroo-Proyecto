from flask import Flask, jsonify, request
from flask_cors import CORS
from ssh import Ssh


app = Flask(__name__)
CORS(app)

ultimos_datos_vms = {}

@app.route('/api/rendimiento/', methods=['POST', 'GET'])
def recibir_rendimiento_ubuntu():
    global ultimos_datos_vms
    
    if request.method == 'POST':
        data = request.json
        
        if not data:
            return jsonify({"error": "No se han proporcionado datos"}), 400
        
        vm_id = data.get("vm_id")
        
        if vm_id:
            ultimos_datos_vms[vm_id] = data
            
        if data.get("vm_id") == "servidor-ubuntu":
            print("VM Ubuntu")
            print(f'CPU de la VM (Ubuntu): {data.get("cpu_uso")}%')
            print(f'RAM en uso: {data.get("ram_uso")}%')
            print(f'Almacenamiento en uso: {data.get("almacenamiento_uso")}%')
            print(f'Procesos con mayor consumo de memoria: {data.get("procesos")}')
        
        elif data.get("vm_id") == "servidor-debian":
            print("VM Debian")
            print(f'CPU de la VM (Debian): {data.get("cpu_uso")}%')
            print(f'RAM en uso: {data.get("ram_uso")}%')
        
        return jsonify({"mensaje": "Datos recibidos correctamente"}), 200
    
    elif request.method == 'GET':
        return jsonify(ultimos_datos_vms), 200
    
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
