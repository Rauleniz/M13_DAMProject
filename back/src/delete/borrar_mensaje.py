from flask import Blueprint, jsonify, request
from back.db import get_database_connection

eliminar_mensaje_bp = Blueprint('eliminar_mensaje', __name__)

@eliminar_mensaje_bp.route('/conversacion/<int:id_conversacion>/mensaje/<int:id_mensaje>', methods=['DELETE'])
def eliminar_mensaje(id_conversacion, id_mensaje):
    try:
        # Verificar la existencia del mensaje y si pertenece a esa conversación en particular
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM mensaje WHERE id = %s AND id_conversacion = %s", (id_mensaje, id_conversacion))
        mensaje = cursor.fetchone()

        if mensaje:
            # Eliminar el mensaje
            cursor.execute("DELETE FROM mensaje WHERE id = %s", (id_mensaje,))
            connection.commit()
            return jsonify({'mensaje': 'Mensaje eliminado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'El mensaje no existe en la conversación'}), 404
    except Exception as e:
        return jsonify({'mensaje': 'Error al eliminar el mensaje', 'error': str(e)}), 500
