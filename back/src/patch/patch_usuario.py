import bcrypt
from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

patch_usuarios_bp = Blueprint('usuarios_patch', __name__)

@patch_usuarios_bp.route('/usuario/<int:usuario_id>', methods=['PATCH'])
def actualizar_dato_usuario(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
        
        connection = get_database_connection()
 
        data_solicitud = request.json
    
        # Consulta dinámica con el for
        sql = "UPDATE usuario SET "
        params = []
        for key, value in data_solicitud.items():
            if key == 'password':
                value = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())
            sql += f"{key} = %s, "
            params.append(value)
        sql = sql.rstrip(', ')  # Eliminar la última coma
        sql += " WHERE id = %s"
        params.append(usuario_id)
     
        cursor = connection.cursor()
        cursor.execute(sql, params)
        connection.commit()

        # Verificar si se realizó la actualización correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Usuario actualizado correctamente'})
        else:
            return jsonify({'mensaje': 'No se encontró el usuario o no se realizaron cambios'}), 404
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al actualizar usuario'}), 500

@patch_usuarios_bp.route('/usuario/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200