from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

get_ubicacion_bp = Blueprint('get_ubicacion', __name__)

@get_ubicacion_bp.route('/ubicacion/<int:usuario_id>', methods=['GET'])
def obtener_ubicacion(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
        # Conectar a la base de datos
        connection = get_database_connection()

        if connection:
            cursor = connection.cursor()            
            cursor.execute("SELECT * FROM ubicacion WHERE id_usuario = %s", (usuario_id,))
            
            ubicacion = cursor.fetchone()

        # Verificar si se encontró la ubicación para el usuario dado
            if ubicacion:
                ubicacion_dict = {
                    'id': ubicacion[0],
                    'id_usuario': ubicacion[1],
                    'lat': ubicacion[2],
                    'lng': ubicacion[3],
                    'descripcion': ubicacion[4],
                    'link1': ubicacion[5],
                    'link2': ubicacion[6],
                    'link3': ubicacion[7],
                    'link4': ubicacion[8]
                }
                return jsonify(ubicacion_dict), 200
            else:
                return jsonify({'mensaje': 'Ubicación no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'No se encontró ubicación para el usuario dado'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener ubicación: {str(e)}"}), 500


@get_ubicacion_bp.route('/ubicacion/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200