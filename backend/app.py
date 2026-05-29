from flask import Flask
from flask_cors import CORS
from routes.rendimientoRoutes import rendimiento_bp
from routes.comandoRoutes import comando_bp
from routes.configuracionRoutes import configuracion_bp
from routes.vmsRoutes import vms_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(rendimiento_bp)

app.register_blueprint(comando_bp)

app.register_blueprint(configuracion_bp)

app.register_blueprint(vms_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
