from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/rendimiento/', methods=['POST'])
def recibir_rendimiento_ubuntu():
    data = request.json
    
    if not data:
        return jsonify({"error": "No se han proporcionado datos"}), 400
    
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
