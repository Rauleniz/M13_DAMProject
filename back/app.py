import os
import sys
import importlib
from flask import Flask

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

app = Flask(__name__)

blueprints = [
    {'module': 'back.src.get.get_usuario', 'name': 'get_usuarios_bp', 'url_prefix': '/get'},
    {'module': 'back.src.put.put_usuario', 'name': 'put_usuarios_bp', 'url_prefix': '/put'},
    {'module': 'back.src.get.get_plan', 'name': 'get_plan_bp', 'url_prefix': '/get'},
    # Agrega aquí todos tus blueprints...
]

for bp in blueprints:
    module = importlib.import_module(bp['module'])
    blueprint = getattr(module, bp['name'])
    app.register_blueprint(blueprint, url_prefix=bp['url_prefix'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)