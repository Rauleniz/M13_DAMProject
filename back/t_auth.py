from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from .models import Usuario
from db import get_database_connection

app = Flask(__name__)

# Configurar la clave secreta para firmar tokens JWT
app.config['JWT_SECRET_KEY'] = 'DamM13&Proj3ct'

# Inicializar la extensión JWTManager con la aplicación Flask
jwt = JWTManager(app)

@app.route('/auth/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Verificar si el usuario ya existe en la base de datos
    if Usuario.query.filter_by(username=username).first():
        return jsonify({'message': 'El usuario ya existe'}), 400

    # Crear un nuevo usuario
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, password))
    connection.commit()

    # Crear y devolver el token de acceso
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

if __name__ == '__main__':
    app.run(debug=True)
