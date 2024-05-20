from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

put_ubicacion_bp = Blueprint('put_ubicacion', __name__)

@put_ubicacion_bp.route('/ubicacion/<int:usuario_id>', methods=['PUT'])
def actualizar_ubicacion(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
        
        # Conectar a la base de datos
        connection = get_database_connection()
        
        data_solicitud = request.json
        lat = data_solicitud.get('tarjeta_lat')
        lng = data_solicitud.get('tarjeta_lng')
        descripcion = data_solicitud.get('tarjeta_descripcion')
        link1 = data_solicitud.get('tarjeta_redes1')
        link2 = data_solicitud.get('tarjeta_redes2')
        link3 = data_solicitud.get('tarjeta_redes3')
        link4 = data_solicitud.get('tarjeta_redes4')

        cursor = connection.cursor()

        # Actualizar la ubicación en la tabla de ubicaciones
        cursor.execute("UPDATE ubicacion SET lat = %s, lng = %s, descripcion = %s, link1 = %s, link2 = %s, link3 = %s, link4 = %s WHERE id_usuario = %s",
                       (lat, lng, descripcion, link1, link2, link3, link4, usuario_id))
        
        connection.commit()

        # Verificar si la ubicación se ha actualizado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Ubicación actualizada correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar la ubicación'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar la ubicación: {str(e)}"}), 500

@put_ubicacion_bp.route('/ubicacion/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200