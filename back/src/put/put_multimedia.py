from flask import Blueprint, jsonify, request
from back.db import get_database_connection

actualizar_multimedia_bp = Blueprint('multimedia_put', __name__)

@actualizar_multimedia_bp.route('/multimedia/<int:multimedia_id>', methods=['PUT'])
def actualizar_multimedia(multimedia_id):
    try:
        # Obtener los datos del cuerpo de la solicitud
        data = request.json
        img = data.get('img')
        song = data.get('song')

        # Conectar a la base de datos
        connection = get_database_connection()
        
        cursor = connection.cursor()
        cursor.execute("UPDATE multimedia SET img=%s, song=%s WHERE id=%s",
                       (img, song, multimedia_id))
        connection.commit()

        # Verificar si se ha actualizado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Multimedia actualizado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar multimedia'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar multimedia: {str(e)}"}), 500
