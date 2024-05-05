from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from auth import verificar_credenciales_decorador
from models import Usuario
from back import db

actualizar_usuario_bp = Blueprint('actualizar_usuario', __name__)

@actualizar_usuario_bp.route('/usuario/actualizar', methods=['PATCH'])
@verificar_credenciales_decorador
def actualizar_usuario(usuario):
    try:
        # Obtener el usuario de la base de datos utilizando su ID
        usuario_a_actualizar = Usuario.query.get(usuario['id'])

        # Verificar si se encontró el usuario
        if usuario_a_actualizar:
            # Actualizar los campos del usuario si se proporcionaron nuevos valores
            # Obtener los datos del usuario del cuerpo de la solicitud
            data = request.json

            # Actualizar los campos del usuario si se proporcionan nuevos valores
            usuario_a_actualizar.nombre = data.get("nombre", usuario_a_actualizar.nombre)
            usuario_a_actualizar.apellido = data.get("apellido", usuario_a_actualizar.apellido)
            usuario_a_actualizar.email = data.get("email", usuario_a_actualizar.email)
            usuario_a_actualizar.direccion = data.get("direccion", usuario_a_actualizar.direccion)
            usuario_a_actualizar.descripcion = data.get("descripcion", usuario_a_actualizar.descripcion)
            usuario_a_actualizar.estatus = data.get("estatus", usuario_a_actualizar.estatus)
            usuario_a_actualizar.username = data.get("username", usuario_a_actualizar.username)
            usuario_a_actualizar.password = data.get("password", usuario_a_actualizar.password)

            
            # Confirmar los cambios en la base de datos
            db.session.commit()

            # Respuesta de éxito
            return jsonify({'mensaje': 'Usuario actualizado correctamente'}), 200
        else:
            # Si no se encuentra el usuario
            return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    except Exception as e:
        # Manejo de errores
        return jsonify({'mensaje': 'Error al actualizar el usuario', 'error': str(e)}), 500
