# En usuarios.py

import token
from flask import Blueprint, current_app, jsonify, render_template, request
import jwt
from back.db import get_database_connection
from config import Config

get_usuarios_bp = Blueprint('usuarios_get', __name__)



@get_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['GET', 'OPTIONS'])
def obtener_usuario(id_usuario):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:        
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        id_usuario = data['sub']
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (id_usuario,))

            usuario = cursor.fetchone()  # Obtener el usuario encontrado
         
            if usuario:
                # return render_template('front/miperfil.html', usuario=usuario)
                return jsonify(usuario)
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener usuario'}), 500


@get_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['OPTIONS'])
def options_usuario(id_usuario):
    return jsonify({'mensaje': 'OK'}), 200