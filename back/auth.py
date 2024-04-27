from flask import Flask, jsonify, request
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

SECRET_KEY = 'tu_clave_secreta'

# Lógica de inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    # Verificar las credenciales del usuario
    # Generar el token JWT
    payload = {'usuario_id': 123, 'exp': datetime.utcnow() + timedelta(minutes=30)}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token})


