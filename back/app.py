import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from flask import Flask
from back.src.get.get_usuario import get_usuarios_bp as usuarios_get_bp
# from post.nuevos_usuarios import nuevos_usuarios_bp as usuarios_post_bp
from back.src.put.put_usuario import put_usuarios_bp as usuarios_put_bp
# from delete.eliminar_usuarios import eliminar_usuarios_bp as usuarios_delete_bp



app = Flask(__name__)

app.register_blueprint(usuarios_get_bp, url_prefix='/get')
app.register_blueprint(usuarios_put_bp, url_prefix='/put')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
