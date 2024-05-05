from flask import Blueprint, request, jsonify
from back.db import get_database_connection

obtener_conversacion_bp = Blueprint('obtener_conversacion', __name__)

@obtener_conversacion_bp.route('/conversacion', methods=['GET'])
def obtener_conversaciones():
    try:
        # Obtener los IDs de los usuarios involucrados de los parámetros de la consulta
        id_usuario1 = request.args.get('id_usuario1', type=int)
        id_usuario2 = request.args.get('id_usuario2', type=int)
        print(id_usuario1, id_usuario2)
        
        # Verificar si la conversación existe y si el usuario pertenece a ella
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM conversacion WHERE (id_usuario1 = %s AND id_usuario2 = %s) OR (id_usuario1 = %s AND id_usuario2 = %s)", (id_usuario1, id_usuario2, id_usuario2, id_usuario1))
        conversaciones = cursor.fetchall()

        if conversaciones:
            return jsonify(conversaciones), 200
        else:
            return jsonify({'mensaje': 'No se encontraron conversaciones'}), 404
    except Exception as e:
        print(f"Error al obtener las conversaciones: {e}")
        return jsonify({'mensaje': 'Error al obtener las conversaciones', 'error': str(e)}), 500



@obtener_conversacion_bp.route('/conversacion/<int:id_conversacion>', methods=['GET'])
def obtener_conversacion_por_id(id_conversacion):
    try:
        # Verificar si la conversación existe
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM conversacion WHERE id = %s", (id_conversacion,))
        conversacion = cursor.fetchone()

        if conversacion:
            return jsonify(conversacion), 200
        else:
            return jsonify({'mensaje': 'Conversación no encontrada'}), 404
    except Exception as e:
        return jsonify({'mensaje': 'Error al obtener la conversación', 'error': str(e)}), 500
