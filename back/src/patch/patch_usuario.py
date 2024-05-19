import bcrypt
from flask import Blueprint, jsonify, request
from back.db import get_database_connection

patch_usuarios_bp = Blueprint('usuarios_patch', __name__)

@patch_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['PATCH'])
def actualizar_dato_usuario(id_usuario):
    connection = get_database_connection()
    try:
        # Obtener los datos del usuario del cuerpo de la solicitud
        data = request.json

        # Crear la consulta SQL de actualización basada en los datos proporcionados
        sql = "UPDATE usuario SET "
        params = []
        for key, value in data.items():
            if key == 'password':
                value = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())
            sql += f"{key} = %s, "
            params.append(value)
        sql = sql.rstrip(', ')  # Eliminar la última coma
        sql += " WHERE id = %s"
        params.append(id_usuario)

        # Actualizar el usuario en la base de datos
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
