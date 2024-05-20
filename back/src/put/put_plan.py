# En usuarios.py

from flask import Blueprint, current_app, jsonify, request, session
import jwt
from db import database

update_plan_bp = Blueprint('update_put', __name__)


@update_plan_bp.route('/plan/<int:usuario_id>', methods=['PUT'])
def actualizar_plan_usuario(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
        
        # Obtener el ID del plan seleccionado por el usuario desde los datos enviados en la solicitud
        data_solicitud = request.json
        nuevo_id_plan = data_solicitud.get('tarjeta_plan')

        # Actualizar el plan del usuario en la base de datos
        cursor = database.cursor()
        sql = "UPDATE usuario SET id_plan = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_id_plan, usuario_id))
        database.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Plan de Suscripción actualizado correctamente'})
        else:
            return jsonify({'mensaje': 'No se encontró el usuario o no se realizaron cambios'}), 404

    except Exception as e:
        print(f"Error al actualizar el Plan de Suscripción: {e}")
        return jsonify({'mensaje': 'Se produjo un error al actualizar el Plan de Suscripción'}), 500


@update_plan_bp.route('/usuario/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200    
