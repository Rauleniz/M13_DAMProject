from flask import Blueprint, jsonify
from back.db import get_database_connection

get_multimedia_bp = Blueprint('multimedia_get', __name__)

@get_multimedia_bp.route('/multimedia/<int:id_usuario>', methods=['GET'])
def obtener_multimedia(id_usuario):
    try:
        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Obtener multimedia del usuario específico
        cursor.execute("SELECT * FROM multimedia WHERE id_usuario = %s", (id_usuario,))
        multimedia = cursor.fetchall()

        if multimedia:
            return jsonify(multimedia), 200
        else:
            return jsonify({'mensaje': 'Multimedia no encontrada para el usuario'}), 404
    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener multimedia: {str(e)}"}), 500
