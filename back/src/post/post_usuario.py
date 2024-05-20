from flask import Blueprint, current_app, jsonify, request
import bcrypt
# import jwt
from back.db import get_database_connection

post_usuarios_bp = Blueprint('usuarios_post', __name__)

@post_usuarios_bp.route('/usuario', methods=['POST'])
def nuevo_usuario():

    connection = get_database_connection()

    try:        
        data = request.json      

        nombre = data.get('nombre_artista')
        apellidos = data.get('apellido_artista')
        email = data.get('email')
        direccion = data.get('direccion_facturacion')
        estatus = data.get('opciones_perfil')
        id_plan = data.get('plan')
        num_tarjeta = data.get('num_tarjeta')
        nombre_tarjeta = data.get('nombre_titular')
        caducidad_tarjeta = data.get('caducidad_tarjeta')
        cvc_tarjeta = data.get('cvc_tarjeta')
        username = data.get('nombre_usuario')
        password = data.get('password')

        # Aplicar el hash bcrypt a la contraseña
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        current_app.logger.info(f'Print de pass hasheado: {hashed_password}')
        current_app.logger.error(f'Print de pass hasheado: {hashed_password}')
  
        cursor = connection.cursor()
        sql = "INSERT INTO usuario (nombre, apellidos, email, direccion, estatus, id_plan, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (nombre, apellidos, email, direccion, estatus, id_plan, username, hashed_password))
        id_usuario = cursor.lastrowid

        sql2 = "INSERT INTO datosbancarios (id_usuario, titular_tarjeta, numero_tarjeta, caducidad_tarjeta, cvc) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql2, (id_usuario, num_tarjeta, nombre_tarjeta, caducidad_tarjeta, cvc_tarjeta))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Usuario dado de alta correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se ha guardado los cambios'}), 404
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al dar de alta el usuario'}), 500
    
    
# @post_usuarios_bp.route('/usuario/<int:usuario_id>', methods=['OPTIONS'])
# def options_usuario(usuario_id):
#     return jsonify({'mensaje': 'OK'}), 200
