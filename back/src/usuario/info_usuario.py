from flask import Blueprint, jsonify
from back.db import get_database_connection
from auth import verificar_credenciales_decorador

usuario_info_bp = Blueprint('usuario_info', __name__)

# @usuario_info_bp.route('/usuario/info', methods=['OPTIONS'])
# def handle_preflight():
#     response = jsonify({'message': 'Preflight request success'})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', '*')
#     response.headers.add('Access-Control-Allow-Methods', '*')
#     return response

# Endpoint para obtener la información del usuario y mostrarla en el frontend en MI PERFIL
@usuario_info_bp.route('/usuario/info', methods=['GET'])
@verificar_credenciales_decorador
def obtener_informacion_usuario(usuario):
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (usuario['id'],))

            usuario = cursor.fetchone() 
            if usuario:
                # Convertir la información del usuario a un diccionario
                info_usuario = {
                    'direccion': usuario['direccion'],
                    'email': usuario['email'],
                    'descripcion': usuario['descripcion'],
                    'link_rss': usuario['link_rss']
                    # Agrega otros campos de información del usuario según sea necesario
                }
                return jsonify(info_usuario), 200
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener usuario'}), 500
