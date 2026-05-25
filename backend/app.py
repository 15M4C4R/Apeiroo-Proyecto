from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hola')
def hola():
    return jsonify({"mensaje": "¡Conexión exitosa con Flask!"})

@app.route('/api/rendimiento/ubuntu', methods=['POST'])
def recibir_rendimiento_ubuntu():
    data = request.json
    
    if not data:
        return jsonify({"error": "No se han proporcionado datos"}), 400
    
    print(f"CPU de la VM (Ubuntu): {data.get('cpu_uso')}%")
    print(f"RAM en uso: {data.get('ram_uso')}%")
    
    return jsonify({"mensaje": "Datos recibidos correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
