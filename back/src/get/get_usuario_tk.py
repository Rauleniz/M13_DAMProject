# En usuarios.py

from flask import Blueprint, jsonify, render_template
# from back.auth import login
from back.db import get_database_connection
from flask_jwt_extended import jwt_required, get_jwt_identity

get_usuarios_tk_bp = Blueprint('usuarios_tk_get', __name__)



@get_usuarios_tk_bp.route('/profile', methods=['GET'])
@jwt_required()
def obtener_usuario(id_usuario):

    id_usuario = get_jwt_identity()
    print(f'/*/*/*/ Print de id_usuario{id_usuario}')
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (id_usuario,))

            usuario = cursor.fetchone()  # Obtener el usuario encontrado
         
            if usuario:
                # return render_template('front/miperfil.html', usuario=usuario)
                return jsonify(usuario)
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener usuario'}), 500

        
