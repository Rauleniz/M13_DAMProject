from flask import Flask, Blueprint, request, jsonify, current_app
import jwt
from datetime import datetime, timedelta
import bcrypt
from db import get_database_connection
from flask_jwt_extended import create_access_token

app = Flask(__name__)
# CORS(app, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], resources={r"/*": {"origins": "*"}})


auth_bp = Blueprint('auth_psw', __name__)


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



def verificar_credenciales_decorador(f):
    def wrapper(*args, **kwargs):
        datos_login = request.json
        username = datos_login.get('username')
        password = datos_login.get('password')
        usuario = verificar_credenciales(username, password)
        if usuario:
            return f(usuario, *args, **kwargs)
        else:
            return jsonify({'mensaje': '**/Credenciales incorrectas'}), 401
    return wrapper



@auth_bp.route('/login', methods=['POST'])
@verificar_credenciales_decorador
def login(usuario):
    try:
          # Generar el token JWT si las credenciales son válidas
        exp_time = datetime.utcnow() + timedelta(minutes=30)
        exp_time_unix = exp_time.timestamp()  # Convertir a tiempo UNIX
        payload = {'usuario_id': usuario['id'], 'exp': exp_time_unix}        
        # Codificar la clave secreta en bytes
        secret_key_bytes = current_app.config['SECRET_KEY'].encode('utf-8')

        # Generar el token JWT utilizando la clave secreta codificada
        token = jwt.encode(payload, secret_key_bytes, algorithm='HS256')

        return jsonify({'token': token}), 200  # Decodificar el token a cadena
    except Exception as e:
        print("Error al generar el token JWT:", e)
        return jsonify({'mensaje': 'Error interno del servidor'}), 500