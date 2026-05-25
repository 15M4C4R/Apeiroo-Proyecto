from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hola')
def hola():
    return jsonify({"mensaje": "¡Conexión exitosa con Flask!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
