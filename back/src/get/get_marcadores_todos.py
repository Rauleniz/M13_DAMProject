from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

get_marcadores_bp = Blueprint('get_marcadores', __name__)

@get_marcadores_bp.route('/marcadores', methods=['GET'])
def obtener_marcadores():

    try:     
        connection = get_database_connection()

        if connection:
            cursor = connection.cursor()            
            cursor.execute("SELECT * FROM ubicacion")
            
            ubicaciones = cursor.fetchall()

        # Verificar si se encontró la ubicación del usuario
            if ubicaciones:
                ubicaciones_dict = [{
                    'id': ubicacion[0],
                    'id_usuario': ubicacion[1],
                    'lat': ubicacion[2],
                    'lng': ubicacion[3],
                    'descripcion': ubicacion[4],
                    'link1': ubicacion[5],
                    'link2': ubicacion[6],
                    'link3': ubicacion[7],
                    'link4': ubicacion[8]
                } for ubicacion in ubicaciones]
                return jsonify(ubicaciones_dict), 200
            else:
                return jsonify({'mensaje': 'Marcadores no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'No se encontró marcadores para el usuario'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener marcadores: {str(e)}"}), 500
