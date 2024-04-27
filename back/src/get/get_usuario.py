# En usuarios.py

from flask import Blueprint, jsonify
from back.db import database

get_usuarios_bp = Blueprint('usuarios_get', __name__)

#usuarios = []

# @get_usuarios_bp.route('/usuario', methods=['GET'])
# def obtener_usuarios():

#     return jsonify(usuarios)

@get_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    try:
        cursor = database.cursor()
        # sql = "SELECT * FROM usuario WHERE id = %s"
        # data = (id_usuario)
        cursor.execute("SELECT * FROM usuario WHERE id = %s", (id_usuario,))

        usuario = cursor.fetchone()  # Obtener el usuario encontrado
        if usuario:
            return jsonify(usuario)
        else:
            return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener usuario'}), 500

        
