from flask import Blueprint, jsonify, request
import bcrypt
from back.db import get_database_connection

post_plan_bp = Blueprint('plan_post', __name__)

@post_plan_bp.route('/plan', methods=['POST'])
def nuevo_plan():
    connection = get_database_connection()
    try:    
        data = request.json
        nombre = data.get('nombre')
        cambio_plan = data.get('cambio_plan')
  
        cursor = connection.cursor()
        sql = "INSERT INTO plan (nombre, cambio_plan) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, cambio_plan))
        connection.commit()

        # Obtener el ID del plan recién insertado
        plan_id = cursor.lastrowid

        # Insertar una entrada en la tabla plan_servicio
        cursor.execute("INSERT INTO plan_servicio (id_plan, id_servicio) VALUES (%s, %s)",
                       (plan_id, data.get('id_servicio')))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Plan dado de alta correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se ha guardado los cambios'}), 404
    except Exception as e:
        print(f"Error al crear plan: {e}")
        return jsonify({'mensaje': 'Se produjo un error al dar de alta el plan'}), 500
