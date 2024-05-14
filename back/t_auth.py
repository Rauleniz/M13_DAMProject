from flask import Flask, Blueprint, request, jsonify, make_response
import bcrypt
from db import get_database_connection

app = Flask(__name__)
t_auth_bp = Blueprint('t_auth_psw', __name__)

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
        datos_login = request.form
        username = datos_login.get('username')
        password = datos_login.get('password')
        usuario = verificar_credenciales(username, password)
        if usuario:
            # Si las credenciales son válidas, establecer una cookie de sesión
            response = make_response(f(usuario, *args, **kwargs))
            response.set_cookie('usuario_id', str(usuario['id']), max_age=365*24*60*60)  # Cookie válida por un año
            return response
        else:
            return jsonify({'mensaje': 'Credenciales incorrectas'}), 401
    return wrapper

# Ruta para el proceso de inicio de sesión
@t_auth_bp.route('/logincookies', methods=['POST'])
@verificar_credenciales_decorador
def login(usuario):
    return jsonify({'mensaje': 'Inicio de sesión exitoso', 'usuario_id': usuario['id']}), 200

