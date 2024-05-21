from flask import Blueprint, current_app, jsonify, request, session
import jwt
from back.auth import verificar_credenciales_decorador
from back.db import get_database_connection

put_bancarios_bp = Blueprint('bancarios_put', __name__)

@put_bancarios_bp.route('/bancario/<int:usuario_id>', methods=['PUT'])
@verificar_credenciales_decorador
def actualizar_datos_bancarios(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401   

    connection = get_database_connection()

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']

        data_solicitud = request.json
        titular_tarjeta = data_solicitud.get('tarjeta_titular')
        numero_tarjeta = data_solicitud.get('tarjeta_numeracion')
        caducidad_tarjeta = data_solicitud.get('tarjeta_fecha_caducidd')
        cvc = data_solicitud.get('tarjeta_cvc')

        cursor = connection.cursor()
        sql = "UPDATE datosbancarios SET titular_tarjeta = %s, numero_tarjeta = %s, caducidad_tarjeta = %s, cvc = %s WHERE id_usuario = %s"
        cursor.execute(sql, (titular_tarjeta, numero_tarjeta, caducidad_tarjeta, cvc, usuario_id))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Datos bancarios actualizados correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se han actualizado los datos bancarios'}), 404
    except Exception as e:
        print(f"Error al actualizar los datos bancarios: {e}")
        return jsonify({'mensaje': 'Se produjo un error al actualizar los datos bancarios'}), 500
    
@put_bancarios_bp.route('/bancario/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200