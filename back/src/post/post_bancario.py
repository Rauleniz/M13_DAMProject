from flask import Blueprint, current_app, jsonify, request, session
import jwt
from back.db import get_database_connection

post_bancarios_bp = Blueprint('bancarios_post', __name__)

@post_bancarios_bp.route('/bancario/<int:usuario_id>', methods=['POST'])
def nuevo_datobancario(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401


    connection = get_database_connection()

    try:    
        data_token = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data_token['sub']

        data_solicitud = request.json
        titular_tarjeta = data_solicitud.get('tarjeta_titular')
        numero_tarjeta = data_solicitud.get('tarjeta_numeracion')
        caducidad_tarjeta = data_solicitud.get('tarjeta_fecha_caducidd')
        cvc = data_solicitud.get('tarjeta_cvc')
  
        cursor = connection.cursor()
        sql = "INSERT INTO datosbancarios (id_usuario, titular_tarjeta, numero_tarjeta, caducidad_tarjeta, cvc) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (usuario_id, titular_tarjeta, numero_tarjeta, caducidad_tarjeta, cvc))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Datos Bancarios dados de alta correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se ha guardado los datos bancarios'}), 404
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al dar de alta los datos bancarios'}), 500

@post_bancarios_bp.route('/bancario/<int:id_usuario>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200