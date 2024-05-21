from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

get_multimedia_bp = Blueprint('multimedia_get', __name__)

@get_multimedia_bp.route('/multimedia/<int:usuario_id>', methods=['GET'])
def obtener_multimedia(usuario_id):
        
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
     
        connection = get_database_connection()
        cursor = connection.cursor()

      
        cursor.execute("SELECT * FROM multimedia WHERE id_usuario = %s", (usuario_id,))
        multimedia = cursor.fetchall()

        if multimedia:
            return jsonify(multimedia), 200
        else:
            return jsonify({'mensaje': 'Multimedia no encontrada para el usuario'}), 404
    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener multimedia: {str(e)}"}), 500

@get_multimedia_bp.route('/multimedia/<int:usuario_id>', methods=['OPTIONS'])
def options_multimedia(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200