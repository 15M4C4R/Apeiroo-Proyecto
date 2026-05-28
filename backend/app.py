from flask import Flask
from flask_cors import CORS
from backend.routes.rendimientoRoutes import rendimiento_bp
from backend.routes.comandoRoutes import comando_bp


app = Flask(__name__)
CORS(app)

app.register_blueprint(rendimiento_bp)

app.register_blueprint(comando_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
