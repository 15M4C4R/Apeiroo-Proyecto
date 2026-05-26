from flask import Flask, jsonify, request
from flask_cors import CORS

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
            print(f'Últimos datos de la VM {vm_id}: {ultimos_datos_vms[vm_id]}')
        
        if data.get("vm_id") == "servidor-ubuntu":
            print("VM Ubuntu")
            print(f'CPU de la VM (Ubuntu): {data.get("cpu_uso")}%')
            print(f'RAM en uso: {data.get("ram_uso")}%')
            print(f'Almacenamiento en uso: {data.get("almacenamiento_uso")}%')
        
        elif data.get("vm_id") == "servidor-debian":
            print("VM Debian")
            print(f'CPU de la VM (Debian): {data.get("cpu_uso")}%')
            print(f'RAM en uso: {data.get("ram_uso")}%')
        
        return jsonify({"mensaje": "Datos recibidos correctamente"}), 200
    
    elif request.method == 'GET':
        return jsonify(ultimos_datos_vms), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
