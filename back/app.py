import os
import sys
import importlib
from flask import Flask #render_template
from flask_cors import CORS #cross_origin
from auth import auth_bp
from flask_sqlalchemy import SQLAlchemy
#import middleware as middleware


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

rutas = ["http://localhost:5500", "http://127.0.0.1:5500"]

app = Flask(__name__)
CORS(app, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], resources={r"/*": {"origins": rutas}}, methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])

app.config['CORS_LOGGING'] = True

app.config['SECRET_KEY'] = 'DamM13&Proj3ct'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/m13db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suprime la señalización de modificaciones de la base de datos

db = SQLAlchemy(app)

# Traemos los blueprints de todos los endpoints
blueprints = [
    {'module': 'back.src.get.get_usuario', 'name': 'get_usuarios_bp', 'url_prefix': '/get'},
    {'module': 'back.src.put.put_usuario', 'name': 'put_usuarios_bp', 'url_prefix': '/put'},
    {'module': 'back.src.post.post_usuario', 'name': 'post_usuarios_bp', 'url_prefix': '/post'},
    {'module': 'back.src.delete.borrar_usuario', 'name': 'delete_usuarios_bp', 'url_prefix': '/delete'},
    {'module': 'back.src.get.get_plan', 'name': 'get_plan_bp', 'url_prefix': '/get'},
    {'module': 'back.src.post.post_plan', 'name': 'post_plan_bp', 'url_prefix': '/post'},
    {'module': 'back.src.post.post_mensaje', 'name': 'escribir_mensaje_bp', 'url_prefix': '/post'},
    {'module': 'back.src.get.get_conversacion', 'name': 'obtener_conversacion_bp', 'url_prefix': '/get'},
    {'module': 'back.src.post.post_conversacion', 'name': 'crear_conversacion_bp', 'url_prefix': '/post'},

    {'module': 'back.src.delete.borrar_plan', 'name': 'delete_plan_bp', 'url_prefix': '/delete'},
    {'module': 'back.src.post.post_bancario', 'name': 'post_bancarios_bp', 'url_prefix': '/post'},
    {'module': 'back.src.usuario.actualizar_nombre', 'name': 'actualizar_nombre_bp', 'url_prefix': '/usuario'},
    {'module': 'back.src.get.credenciales_get_usuario', 'name': 'usuario_info_bp', 'url_prefix': '/get'},   
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
    print (f'Vamosssssss')
    return f'exitooooo'


if __name__ == '__main__':
    app.run(debug=True, port=5000)