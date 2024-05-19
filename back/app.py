import os
import sys
import importlib
from flask import Flask, jsonify #render_template
from flask_cors import CORS 
from flask_jwt_extended import JWTManager #cross_origin
from auth import auth_bp
from flask_sqlalchemy import SQLAlchemy
from mysql.connector import pooling
#import middleware as middleware
import logging
from logging.handlers import RotatingFileHandler
from socketio_config import socketio


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

rutas = ["http://localhost:5500", "http://127.0.0.1:5500"]

app = Flask(__name__)
CORS(app, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], resources={r"/*": {"origins": rutas}}, methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])

app.config['SECRET_KEY'] = 'DamM13&Pr0j3c7'
app.config['JWT_TOKEN_LOCATION'] = ['headers']

app.config['CORS_LOGGING'] = True


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/m13db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suprime la señalización de modificaciones de la base de datos

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Configuración de Logging
if not app.debug:
    # Manejador que rota los logs cuando alcanzan cierto tamaño
    handler = RotatingFileHandler('./logs/app.log', maxBytes=10000, backupCount=3) 
    app.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

# DESCOMENTAR para saber en qué nivel de logging estamos: NOTSET: 0 DEBUG: 10 INFO: 20 WARNING: 30 ERROR: 40 CRITICAL: 50
# nivel_logging = app.logger.getEffectiveLevel()
# app.logger.warning(f"El nivel de logging actual es: {nivel_logging}")
        

# Traemos los blueprints de todos los endpoints
blueprints = [
    {'module': 'back.src.get.get_usuario', 'name': 'get_usuarios_bp', 'url_prefix': '/get'},
    {'module': 'back.src.get.get_plan', 'name': 'get_plan_bp', 'url_prefix': '/get'},
    {'module': 'back.src.get.get_conversacion', 'name': 'obtener_conversacion_bp', 'url_prefix': '/get'},
    {'module': 'back.src.get.get_factura', 'name': 'get_factura_usuario_bp', 'url_prefix': '/get'},
    {'module': 'back.src.get.get_multimedia', 'name': 'get_multimedia_bp', 'url_prefix': '/get'},
    {'module': 'back.src.get.get_servicio', 'name': 'get_servicio_bp', 'url_prefix': '/get'},
    {'module': 'back.src.get.get_ubicacion', 'name': 'get_ubicacion_bp', 'url_prefix': '/get'},
    {'module': 'back.src.get.get_agenda', 'name': 'get_agenda_bp', 'url_prefix': '/get'},
    {'module': 'back.src.post.post_usuario', 'name': 'post_usuarios_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_mensaje', 'name': 'escribir_mensaje_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_plan', 'name': 'post_plan_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_conversacion', 'name': 'crear_conversacion_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_bancario', 'name': 'post_bancarios_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_factura', 'name': 'crear_factura_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_multimedia', 'name': 'post_multimedia_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_servicio', 'name': 'post_servicio_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_ubicacion', 'name': 'post_ubicacion_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_agenda', 'name': 'post_agenda_bp', 'url_prefix': '/post'},
    {'module': 'back.src.put.put_factura', 'name': 'actualizar_factura_bp', 'url_prefix': '/put'},
    {'module': 'back.src.put.put_usuario', 'name': 'put_usuarios_bp', 'url_prefix': '/put'},
    {'module': 'back.src.patch.patch_usuario', 'name': 'patch_usuarios_bp', 'url_prefix': '/patch'},
    {'module': 'back.src.put.put_bancario', 'name': 'put_bancarios_bp', 'url_prefix': '/put'},
    {'module': 'back.src.put.put_multimedia', 'name': 'actualizar_multimedia_bp', 'url_prefix': '/put'},
    {'module': 'back.src.put.put_servicio', 'name': 'put_servicio_bp', 'url_prefix': '/put'},
    {'module': 'back.src.put.put_ubicacion', 'name': 'put_ubicacion_bp', 'url_prefix': '/put'},
    {'module': 'back.src.delete.borrar_usuario', 'name': 'delete_usuarios_bp', 'url_prefix': '/delete'},
    {'module': 'back.src.delete.borrar_conversacion', 'name': 'delete_conversacion_bp', 'url_prefix': '/delete'},
    {'module': 'back.src.delete.borrar_mensaje', 'name': 'eliminar_mensaje_bp', 'url_prefix': '/delete'},
    {'module': 'back.src.delete.borrar_plan', 'name': 'delete_plan_bp', 'url_prefix': '/delete'}, 

]



# Para atender la solicitud recorremos los blueprints en función del endpoint seleccionado
for bp in blueprints:
    module = importlib.import_module(bp['module'])
    blueprint = getattr(module, bp['name'])
    app.register_blueprint(blueprint, url_prefix=bp['url_prefix'])


# Registrando el blueprint de autenticación
app.register_blueprint(auth_bp) 



# 01/05 - VALORAR SI HACER TODOS LOS ENDPOINTS EN EL APP.PY
@app.route('/')
def index():      
    print (f'Conectado')
    return f'Conectado'


@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Error no manejado: {e}")
    return jsonify({'mensaje': 'Se produjo un error interno'}), 500

if __name__ == '__main__':
    #app.secret_key = 'DamM13&Proj3ct'
    socketio.init_app(app)
    app.run(debug=True, port=5000)