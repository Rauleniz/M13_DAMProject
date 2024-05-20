from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection
# from flask_cors import cross_origin


post_ubicacion_bp = Blueprint('post_ubicacion', __name__)

@post_ubicacion_bp.route('/ubicacion/<int:usuario_id>', methods=['POST'])
# @cross_origin()
def agregar_ubicacion(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    connection = get_database_connection()

    try:

        data_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data_token['sub']

        # Obtener los datos de la solicitud
        data = request.json
        lat = data.get('tarjeta_lat')
        lng = data.get('tarjeta_lng')
        descripcion = data.get('tarjeta_descripcion')
        link1 = data.get('tarjeta_redes1')
        link2 = data.get('tarjeta_redes2')
        link3 = data.get('tarjeta_redes3')
        link4 = data.get('tarjeta_redes4')

        # Conectar a la base de datos
        cursor = connection.cursor()
        # Insertar la ubicación en la tabla de ubicaciones
        cursor.execute("INSERT INTO ubicacion (id_usuario, lat, lng, descripcion, link1, link2, link3, link4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (usuario_id, lat, lng, descripcion, link1, link2, link3, link4))
        connection.commit()

        # Verificar si la ubicación se ha insertado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Ubicación agregada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al agregar la ubicación'}), 500

    except Exception as e:
        return jsonify({'mensaje': f"Error al agregar la ubicación: {str(e)}"}), 500
    

@post_ubicacion_bp.route('/ubicacion/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200
