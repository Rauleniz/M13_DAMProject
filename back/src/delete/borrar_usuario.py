
from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

delete_usuarios_bp = Blueprint('usuarios_delete', __name__)



@delete_usuarios_bp.route('/usuario/<int:usuario_id>', methods=['DELETE'])
def borrar_usuario(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401
      
    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']

        data_solicitud = request.json
        tarjeta_suscripcion = data_solicitud.get('tarjeta_suscripcion')
    
        connection = get_database_connection()
        
        if connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE usuario SET id_plan = 'NULL' WHERE id = %s", (usuario_id,))    
            connection.commit()

            if cursor.rowcount > 0:               
                return jsonify({'mensaje': 'Cuenta cancelada'}), 200
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al eliminar usuario'}), 500

        
@delete_usuarios_bp.route('/usuario/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200