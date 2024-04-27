# En usuarios.py

from flask import Blueprint, jsonify, request
from db import database

put_usuarios_bp = Blueprint('usuarios_put', __name__)

usuarios = []


@put_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    try:
        cursor = database.cursor()
        # quedan fuera del UPDATE el id_plan 
        sql = "UPDATE usuario SET nombre = %s, apellidos = %s, email = %s, direccion = %s, descripcion = %s, estatus = %s, username = %s, password = %s WHERE id = %s"
        # Se obtiene el nombre del usuario del cuerpo de la solicitud
        nombre_usuario = request.json.get('nombre')
        apellidos_usuario = request.json.get('apellidos')        
        email_usuario = request.json.get('email')
        direccion_usuario = request.json.get('direccion')
        descripcion_usuario = request.json.get('descripcion')
        estatus_usuario = request.json.get('estatus')
        username_usuario = request.json.get('username')
        password_usuario = request.json.get('password')

        data = (nombre_usuario, apellidos_usuario, email_usuario, direccion_usuario, descripcion_usuario, estatus_usuario, username_usuario, password_usuario, id_usuario)
        cursor.execute(sql, data)
        database.commit()
        # Se verifica si se realizó la actualización correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Usuario actualizado correctamente'})
        else:
            return jsonify({'mensaje': 'No se encontró el usuario o no se realizaron cambios'}), 404
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al actualizar usuario'}), 500


        
