from flask import Blueprint, jsonify, request
from back.db import get_database_connection

put_ubicacion_bp = Blueprint('put_ubicacion', __name__)

@put_ubicacion_bp.route('/ubicacion/<int:ubicacion_id>', methods=['PUT'])
def actualizar_ubicacion(ubicacion_id):
    try:
        # Obtener los datos de la solicitud
        data = request.json
        lat = data.get('lat')
        lng = data.get('lng')
        descripcion = data.get('descripcion')
        link1 = data.get('link1')
        link2 = data.get('link2')
        link3 = data.get('link3')
        link4 = data.get('link4')

        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Actualizar la ubicación en la tabla de ubicaciones
        cursor.execute("UPDATE ubicacion SET lat = %s, lng = %s, descripcion = %s, link1 = %s, link2 = %s, link3 = %s, link4 = %s WHERE id = %s",
                       (lat, lng, descripcion, link1, link2, link3, link4, ubicacion_id))
        connection.commit()

        # Verificar si la ubicación se ha actualizado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Ubicación actualizada correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar la ubicación'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar la ubicación: {str(e)}"}), 500
