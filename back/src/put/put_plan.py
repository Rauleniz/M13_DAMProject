# En usuarios.py

from flask import Blueprint, jsonify, request, session
from db import database

update_plan_bp = Blueprint('update_put', __name__)


@update_plan_bp.route('/usuario/plan', methods=['PUT'])
def actualizar_plan_usuario():
    try:
        # Obtener el ID del usuario que ya ha inciado la sesión:¨session['user_id'] = user_id
        id_usuario = session.get('user_id')
        if id_usuario is None:
            return jsonify({'mensaje': 'Usuario no autenticado'}), 401
        
        # Obtener el ID del plan seleccionado por el usuario desde los datos enviados en la solicitud
        data = request.json
        nuevo_id_plan = data.get('id_plan')

        # Actualizar el plan del usuario en la base de datos
        cursor = database.cursor()
        sql = "UPDATE usuario SET plan_id = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_id_plan, id_usuario))
        database.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Plan de Suscripción actualizado correctamente'})
        else:
            return jsonify({'mensaje': 'No se encontró el usuario o no se realizaron cambios'}), 404

    except Exception as e:
        print(f"Error al actualizar el Plan de Suscripción: {e}")
        return jsonify({'mensaje': 'Se produjo un error al actualizar el Plan de Suscripción'}), 500


        
