"""
Middelware - Script para generar token de autenticación y posteriormente utilizarlo en el resto de scripts
"""

from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

def verificar_token(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'mensaje': 'Token de autenticación requerido'}), 401
        id_usuario = verificar_token(token)
        if id_usuario is None:
            return jsonify({'mensaje': 'Token de autenticación inválido'}), 401
        # Pasar el ID de usuario a la función del endpoint
        return f(id_usuario, *args, **kwargs)
    return decorador

@app.route('/usuario', methods=['GET'])
@verificar_token
def obtener_usuario(id_usuario):
    # Lógica para obtener los datos del usuario
    datos_usuario = obtener_datos_usuario(id_usuario) # hay que definir la función en otro lugar del código
    return jsonify(datos_usuario)
