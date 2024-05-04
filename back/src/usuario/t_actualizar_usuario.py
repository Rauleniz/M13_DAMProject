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
        # Obtener los nuevos datos del usuario del cuerpo de la solicitud
        data = request.json
        nuevo_nombre = data.get('nombre')
        nuevos_apellidos = data.get('apellidos')
        nuevo_email = data.get('email')
        nueva_direccion = data.get('direccion')
        nueva_descripcion = data.get('descripcion')
        nuevo_estatus = data.get('estatus')
        nuevo_username = data.get('username')
        nueva_password = data.get('password')

        # Obtener el usuario de la base de datos utilizando su ID
        usuario_a_actualizar = Usuario.query.get(usuario['id'])

        # Verificar si se encontró el usuario
        if usuario_a_actualizar:
            # Actualizar los campos del usuario si se proporcionaron nuevos valores
            if nuevo_nombre:
                usuario_a_actualizar.nombre = nuevo_nombre
            if nuevos_apellidos:
                usuario_a_actualizar.apellidos = nuevos_apellidos
            if nuevo_email:
                usuario_a_actualizar.email = nuevo_email
            if nueva_direccion:
                usuario_a_actualizar.direccion = nueva_direccion
            if nueva_descripcion:
                usuario_a_actualizar.descripcion = nueva_descripcion
            if nuevo_estatus:
                usuario_a_actualizar.estatus = nuevo_estatus
            if nuevo_username:
                usuario_a_actualizar.username = nuevo_username
            if nueva_password:
                usuario_a_actualizar.password = nueva_password
            
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
