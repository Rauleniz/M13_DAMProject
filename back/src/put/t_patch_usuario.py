from flask import Blueprint, jsonify, request
from models import Usuario  # Importa el modelo de Usuario desde tu archivo models.py
from back import db  # Importa el objeto db que representa la instancia de SQLAlchemy

put_usuarios_bp = Blueprint('usuarios_put', __name__)

@put_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['PATCH'])
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

        # Buscar el usuario en la base de datos
        usuario = Usuario.query.get(id_usuario)

        # Verificar si el usuario existe
        if usuario:
            # Actualizar los atributos del usuario
            usuario.nombre = nombre
            usuario.apellidos = apellidos
            usuario.email = email
            usuario.direccion = direccion
            usuario.descripcion = descripcion
            usuario.estatus = estatus
            usuario.username = username
            usuario.password = password

            # Guardar los cambios en la base de datos
            db.session.commit()

            return jsonify({'mensaje': 'Usuario actualizado correctamente'})
        else:
            return jsonify({'mensaje': 'No se encontró el usuario'}), 404
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al actualizar usuario'}), 500
