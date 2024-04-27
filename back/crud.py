from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)

SECRET_KEY = 'tu_clave_secreta'

# Middleware para verificar el token JWT
def verificar_token(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'mensaje': 'Token no proporcionado'}), 401
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            # Aquí puedes usar la información del usuario del payload
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido'}), 401
    return wrapper

# Ruta protegida
@app.route('/datos', methods=['GET'])
@verificar_token
def obtener_datos():
    # Obtener datos del usuario y responder
    return jsonify({'mensaje': 'Datos protegidos'})

if __name__ == '__main__':
    app.run(debug=True)