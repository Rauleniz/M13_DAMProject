# En usuarios.py

import token
from flask import Blueprint, current_app, jsonify, render_template, request
import jwt
from back.db import get_database_connection
from config import Config

get_usuarios_bp = Blueprint('usuarios_get', __name__)



@get_usuarios_bp.route('/usuario/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:        
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
        current_app.logger.debug(f"Token decodificado: {data}") 
        current_app.logger.debug(f"ID de usuario del token: {usuario_id}") 

        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (usuario_id,))

            usuario = cursor.fetchone()
         
            if usuario:                
                return jsonify(usuario)
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener usuario'}), 500


@get_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200