from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

get_factura_usuario_bp = Blueprint('factura_usuario_get', __name__)

@get_factura_usuario_bp.route('/factura/<int:usuario_id>', methods=['GET'])
def obtener_factura_usuario(usuario_id):
    
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401
    
    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
        current_app.logger.debug(f"Token decodificado: {data}") 
        current_app.logger.debug(f"ID de usuario del token: {usuario_id}") 
     
        connection = get_database_connection()

        # Obtener las facturas del usuario
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM factura WHERE id_usuario = %s", (usuario_id,))
        facturas = cursor.fetchall()

        # Verificar si se encontraron facturas para el usuario
        if facturas:
            return jsonify(facturas), 200
        else:
            return jsonify({'mensaje': 'No se encontraron facturas para el usuario'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener las facturas del usuario: {str(e)}"}), 500


@get_factura_usuario_bp.route('/factura/<int:usuario_id>', methods=['OPTIONS'])
def options_factura_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200