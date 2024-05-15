from flask import Blueprint, jsonify, request
from back.db import get_database_connection

post_ubicacion_bp = Blueprint('post_ubicacion', __name__)

@post_ubicacion_bp.route('/ubicacion', methods=['POST'])
def agregar_ubicacion():
    try:
        # Obtener los datos de la solicitud
        data = request.json
        id_usuario = data.get('id_usuario')
        lat = data.get('lat')
        lng = data.get('lng')
        descripcion = data.get('descripcion')
        link_rrss = data.get('link_rrss')

        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Insertar la ubicación en la tabla de ubicaciones
        cursor.execute("INSERT INTO ubicacion (id_usuario, lat, lng, descripcion, link_rrss) VALUES (%s, %s, %s, %s, %s)",
                       (id_usuario, lat, lng, descripcion, link_rrss))
        connection.commit()

        # Verificar si la ubicación se ha insertado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Ubicación agregada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al agregar la ubicación'}), 500

    except Exception as e:
        return jsonify({'mensaje': f"Error al agregar la ubicación: {str(e)}"}), 500
