from flask import Blueprint, jsonify, request
from back.db import get_database_connection

put_agenda_bp = Blueprint('put_agenda', __name__)

@put_agenda_bp.route('/servicio/<int:usuario_id>', methods=['PUT'])
def actualizar_servicio(usuario_id):
    try:
        # Obtener los datos del servicio del cuerpo de la solicitud
        data = request.json
        usuario_id = data.get('usuario_id')
        fecha = data.get('fecha')
        titulo = data.get('titulo')
        descripcion = data.get('seguro')

        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Actualizar el servicio en la base de datos
        cursor.execute("UPDATE agenda SET usuario_id=%s, fecha=%s, titulo=%s, descripcion=%s WHERE id_usuario=%s",
                       (usuario_id, fecha, titulo, descripcion))
        connection.commit()

        # Verificar si el servicio se ha actualizado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Servicio actualizado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar el servicio'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar el servicio: {str(e)}"}), 500
