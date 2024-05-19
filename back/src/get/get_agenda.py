from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

get_agenda_bp = Blueprint('get_agenda', __name__)

@get_agenda_bp.route('/agenda/<int:usuario_id>', methods=['GET'])
def obtener_ubicacion(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']

        connection = get_database_connection()

        if connection:
            cursor = connection.cursor()            
            cursor.execute("SELECT * FROM agenda WHERE id_usuario = %s", (usuario_id,))
            
            agenda = cursor.fetchone()

            if agenda:
                agenda_dict = {
                    'id': agenda[0],
                    'id_usuario': agenda[1],
                    'fecha': agenda[2],
                    'titulo': agenda[3],
                    'descripcion': agenda[4]
                }
                return jsonify(agenda_dict), 200
            else:
                return jsonify({'mensaje': 'Evento no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'No se encontró la agenda para el usuario dado'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener la agenda: {str(e)}"}), 500


@get_agenda_bp.route('/ubicacion/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200