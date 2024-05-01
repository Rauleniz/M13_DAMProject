from flask import Blueprint, jsonify, make_response, request
from back.db import get_database_connection
from auth import verificar_credenciales_decorador

usuario_info_bp = Blueprint('usuario_info', __name__)

def handle_preflight():
    response = make_response(jsonify({'message': 'Preflight request success'}))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@usuario_info_bp.route('/usuario/info', methods=['OPTIONS'])
def options():
    return handle_preflight()

@usuario_info_bp.route('/usuario/info', methods=['GET'])
@verificar_credenciales_decorador
def obtener_informacion_usuario(usuario):
    try:
        user_id = usuario['id']
        print(f'*/*/*/*/*/*Print de user_id: {user_id}')
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (user_id,))

            usuario = cursor.fetchone() 
            print(f'*/*/*/*/*/*Print de usuario: {usuario}')
            if usuario:
                info_usuario = {
                    'nombre': usuario['nombre'],
                    'apellidos': usuario['apellidos'],
                    'email': usuario['email'],
                    'direccion': usuario['direccion'],
                    'descripcion': usuario['descripcion'],
                    'estatus': usuario['estatus'],
                    'img_perfil': usuario['img_perfil'],
                    'cancion': usuario['cancion'],
                    'id_plan': usuario['id_plan'],
                    'link_rrss': usuario['link_rrss'],
                    'username': usuario['username'],
                    'password': usuario['password']
                }
                print(f'*/*/*/*/*/*Print de la query info_usuario: {info_usuario}')              
                return jsonify(info_usuario), 200
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener usuario'}), 500
    
    finally:
        if connection:
            connection.close()
