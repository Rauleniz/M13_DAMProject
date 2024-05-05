from flask import Blueprint, jsonify, request
from back.db import get_database_connection

put_servicio_bp = Blueprint('put_servicio', __name__)

@put_servicio_bp.route('/servicio/<int:servicio_id>', methods=['PUT'])
def actualizar_servicio(servicio_id):
    try:
        # Obtener los datos del servicio del cuerpo de la solicitud
        data = request.json
        asignacion_tecnico = data.get('asignacion_tecnico')
        cheque = data.get('cheque')
        financiacion = data.get('financiacion')
        seguro = data.get('seguro')
        alquiler_furgon = data.get('alquiler_furgon')

        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Actualizar el servicio en la base de datos
        cursor.execute("UPDATE servicio SET asignacion_tecnico=%s, cheque=%s, financiacion=%s, seguro=%s, alquiler_furgon=%s WHERE id=%s",
                       (asignacion_tecnico, cheque, financiacion, seguro, alquiler_furgon, servicio_id))
        connection.commit()

        # Verificar si el servicio se ha actualizado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Servicio actualizado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar el servicio'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar el servicio: {str(e)}"}), 500
