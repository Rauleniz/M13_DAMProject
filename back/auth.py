from flask import Flask, request, jsonify, current_app
import jwt
from datetime import datetime, timedelta
import bcrypt
from db import database
import mysql.connector

app = Flask(__name__)


def verificar_credenciales(username, password):
    try:
        connection = mysql.connector.connect(**database)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM usuario WHERE username = %s"
            cursor.execute(sql, (username,))
            usuario = cursor.fetchone()
            if usuario:
                # Verificar la contraseña utilizando bcrypt
                hashed_password = usuario['password']
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                    return usuario
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
    finally:
        if 'connection' in locals():
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
            return jsonify({'mensaje': 'Credenciales incorrectas'}), 401
    return wrapper



@app.route('/login', methods=['POST'])
@verificar_credenciales_decorador
def login(usuario):
    try:
        # Generar el token JWT si las credenciales son válidas
        payload = {'usuario_id': usuario['id'], 'exp': datetime.utcnow() + timedelta(minutes=30)}
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200
    except Exception as e:
        print("Error al generar el token JWT:", e)
        return jsonify({'mensaje': 'Error interno del servidor'}), 500
