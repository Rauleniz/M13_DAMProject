from flask import Blueprint, jsonify
from back.db import get_database_connection

get_ubicacion_bp = Blueprint('get_ubicacion', __name__)

@get_ubicacion_bp.route('/ubicacion/<int:id_usuario>', methods=['GET'])
def obtener_ubicacion(id_usuario):
    try:
        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Obtener la información de ubicación para el usuario dado
        cursor.execute("SELECT * FROM ubicacion WHERE id_usuario = %s", (id_usuario,))
        ubicacion = cursor.fetchone()

        # Verificar si se encontró la ubicación para el usuario dado
        if ubicacion:
            ubicacion_dict = {
                'id': ubicacion[0],
                'id_usuario': ubicacion[1],
                'lat': ubicacion[2],
                'lng': ubicacion[3],
                'descripcion': ubicacion[4],
                'link_rrss': ubicacion[5]
            }
            return jsonify(ubicacion_dict), 200
        else:
            return jsonify({'mensaje': 'No se encontró ubicación para el usuario dado'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener ubicación: {str(e)}"}), 500
