from flask import Flask, Blueprint, request, jsonify, current_app
import jwt
from datetime import datetime, timedelta, timezone
import bcrypt
from db import get_database_connection
from flask_jwt_extended import create_access_token, current_user, decode_token
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
auth_bp = Blueprint('auth_psw', __name__)


# Función para verificar las credenciales del usuario en la base de datos
def verificar_credenciales(username, password):
    connection = None
    try:
        connection = get_database_connection()
        if connection:
            with connection.cursor(dictionary=True) as cursor:
                sql = "SELECT id, password FROM usuario WHERE username = %s"
                cursor.execute(sql, (username,))
                usuario = cursor.fetchone()
                if usuario:
                    hashed_password = usuario['password']
                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        return usuario
    except Exception as error:
        print("Error al conectar a la base de datos:", error)
    finally:
        if connection:
            connection.close()
    return None

# Decorador para verificar las credenciales del usuario
def verificar_credenciales_decorador(f):
    def wrapper(*args, **kwargs):
        datos_login = request.json
        username = datos_login.get('username')
        password = datos_login.get('password')
        usuario = verificar_credenciales(username, password)
        if usuario:
            return f(usuario, *args, **kwargs)
        else:
            return jsonify({'mensaje': 'Credenciales incorrectas'}), 401
    return wrapper

# Ruta para el proceso de inicio de sesión
@auth_bp.route('/login', methods=['POST'])
@verificar_credenciales_decorador
def login(usuario):
    try:
        usuario_id = usuario['id']
        current_app.logger.debug(f'Print de usuario_id {usuario_id}')        

        # Generar el token JWT si las credenciales son válidas
        exp_time = datetime.now(
                        tz=timezone.utc
                        ) + timedelta(minutes=60)
        exp_time_unix = exp_time.timestamp()  # Convertir a tiempo UNIX
        payload = {'sub': usuario['id'], 'exp': exp_time_unix}   

        current_app.logger.debug(f'Print de exp_time y :exp_time_unix {exp_time} // {exp_time_unix}')        

        # Codificar la clave secreta en bytes
        secret_key_bytes = current_app.config['SECRET_KEY'].encode('utf-8')
        app.logger.info(f'Print de la Clave Secreta en auth.py: {current_app.config['SECRET_KEY']}')

        # Generar el token JWT utilizando la clave secreta codificada
        token = jwt.encode(payload, secret_key_bytes, algorithm='HS256')   
                

        current_app.logger.info(f"Usuario {usuario_id} ha iniciado sesión exitosamente.")
        current_app.logger.info(f"token {token} de inicio sesión exitosamente.")
        return jsonify({'token': token, 'usuario_id': usuario_id}), 200
    except Exception as e:
        app.logger.error(f"Error al generar el token JWT: {e}")
        return jsonify({'mensaje': 'Error interno del servidor'}), 500




