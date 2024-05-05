
from flask import Blueprint, jsonify
from back.db import get_database_connection

delete_conversacion_bp = Blueprint('conversacion_delete', __name__)



@delete_conversacion_bp.route('/conversacion/<int:id_conversacion>', methods=['DELETE'])
def eliminar_conversacion(id_conversacion):
    try:
        # Verificar la existencia de la conversación
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM conversacion WHERE id = %s", (id_conversacion,))
        conversacion = cursor.fetchone()

        if conversacion:
            # Eliminar la conversación
            cursor.execute("DELETE FROM conversacion WHERE id = %s", (id_conversacion,))
            connection.commit()
            return jsonify({'mensaje': 'Conversación eliminada correctamente'}), 200
        else:
            return jsonify({'mensaje': 'La conversación no existe'}), 404
    except Exception as e:
        return jsonify({'mensaje': 'Error al eliminar la conversación', 'error': str(e)}), 500

        
