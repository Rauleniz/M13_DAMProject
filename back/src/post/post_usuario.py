from flask import Blueprint, jsonify, request
from back.db import database

post_usuarios_bp = Blueprint('usuarios_post', __name__)

@post_usuarios_bp.route('/usuario', methods=['POST'])
def nuevo_usuario():
    try:    
        data = request.json
        nombre = data.get('nombre')
        apellidos = data.get('apellidos')
        email = data.get('email')
        direccion = data.get('direccion')
        descripcion = data.get('descripcion')
        estatus = data.get('estatus')
        id_plan = data.get('id_plan')
        username = data.get('username')
        password = data.get('password')
  
        cursor = database.cursor()
        sql = "INSERT INTO usuario (nombre, apellidos, email, direccion, descripcion, estatus, id_plan, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (nombre, apellidos, email, direccion, descripcion, estatus, id_plan, username, password))
        database.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Usuario dado de alta correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se ha guardado los cambios'}), 404
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al dar de alta el usuario'}), 500
