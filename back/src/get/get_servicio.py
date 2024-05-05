from flask import Blueprint, jsonify
from back.db import get_database_connection

get_servicio_bp = Blueprint('get_servicio', __name__)

@get_servicio_bp.route('/servicio', methods=['GET'])
def obtener_servicios():
    try:
        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Obtener todos los servicios
        cursor.execute("SELECT * FROM servicio")
        servicios = cursor.fetchall()

        # Verificar si se encontraron servicios
        if servicios:
            return jsonify(servicios), 200
        else:
            return jsonify({'mensaje': 'No se encontraron servicios'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener los servicios: {str(e)}"}), 500
