import os
import sys
import importlib
from flask import Flask

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

app = Flask(__name__)

# Traemos los blueprints de todos los endpoints
blueprints = [
    {'module': 'back.src.get.get_usuario', 'name': 'get_usuarios_bp', 'url_prefix': '/get'},
    {'module': 'back.src.put.put_usuario', 'name': 'put_usuarios_bp', 'url_prefix': '/put'},
    {'module': 'back.src.post.post_usuario', 'name': 'post_usuarios_bp', 'url_prefix': '/post'},
    {'module': 'back.src.get.get_plan', 'name': 'get_plan_bp', 'url_prefix': '/get'},
    {'module': 'back.src.post.post_bancario', 'name': 'post_bancarios_bp', 'url_prefix': '/post'},
   
]

# Para atender la solicitud recorremos los blueprints en función del endpoint seleccionado
for bp in blueprints:
    module = importlib.import_module(bp['module'])
    blueprint = getattr(module, bp['name'])
    app.register_blueprint(blueprint, url_prefix=bp['url_prefix'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)