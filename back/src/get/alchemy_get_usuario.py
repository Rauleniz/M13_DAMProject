from flask import Blueprint, jsonify, request
from back.db import get_database_connection
from models import Usuario

alchemy_get_usuarios_bp = Blueprint('usuarios_get_alchemy', __name__)
connection = get_database_connection()

@alchemy_get_usuarios_bp.route('/alchemyusuarios', methods = ['GET'])
def get_usuario():
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario")

            usuario = cursor.fetchall()  # Obtener todos los usuarios encontrado
            if usuario:
                return jsonify(usuario)
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener usuario'}), 500


