from flask import Blueprint, jsonify, request
from back.db import database

put_usuarios_bp = Blueprint('usuarios_put', __name__)

@put_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    try:
        # Obtener los datos del usuario del cuerpo de la solicitud
        data = request.json
        nombre = data.get('nombre')
        apellidos = data.get('apellidos')
        email = data.get('email')
        direccion = data.get('direccion')
        descripcion = data.get('descripcion')
        estatus = data.get('estatus')
        username = data.get('username')
        password = data.get('password')

        # Actualizar el usuario en la base de datos
        cursor = database.cursor()
        sql = "UPDATE usuario SET nombre = %s, apellidos = %s, email = %s, direccion = %s, descripcion = %s, estatus = %s, username = %s, password = %s WHERE id = %s"
        cursor.execute(sql, (nombre, apellidos, email, direccion, descripcion, estatus, username, password, id_usuario))
        database.commit()

        # Verificar si se realizó la actualización correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Usuario actualizado correctamente'})
        else:
            return jsonify({'mensaje': 'No se encontró el usuario o no se realizaron cambios'}), 404
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al actualizar usuario'}), 500
