from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

put_agenda_bp = Blueprint('put_agenda', __name__)

@put_agenda_bp.route('/agenda/<int:usuario_id>', methods=['PUT'])
def actualizar_servicio(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']

        data_solicitud = request.json
        usuario_id = data_solicitud.get('usuario_id')
        fecha = data_solicitud.get('fecha')
        titulo = data_solicitud.get('titulo')
        descripcion = data_solicitud.get('descripcion')

        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("UPDATE agenda SET usuario_id=%s, fecha=%s, titulo=%s, descripcion=%s WHERE id_usuario=%s",
                       (usuario_id, fecha, titulo, descripcion))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Servicio actualizado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar el servicio'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar el servicio: {str(e)}"}), 500

@put_agenda_bp.route('/agenda/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200