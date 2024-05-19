from flask import Blueprint, current_app, jsonify, request
import bcrypt
import jwt
from back.db import get_database_connection

post_plan_bp = Blueprint('plan_post', __name__)

@post_plan_bp.route('/plan/<int:usuario_id>', methods=['POST'])
def nuevo_plan(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    connection = get_database_connection()

    try:    
        data_token = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data_token['sub']
    
        data_solicitud = request.json
        nombre = data_solicitud.get('nombre')
        cambio_plan = data_solicitud.get('cambio_plan')
  
        cursor = connection.cursor()
        sql = "INSERT INTO plan (nombre, cambio_plan) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, cambio_plan))
        connection.commit()

        # Obtener el ID del plan recién insertado
        plan_id = cursor.lastrowid

        # Insertar una entrada en la tabla plan_servicio
        cursor.execute("INSERT INTO plan_servicio (id_plan, id_servicio) VALUES (%s, %s)",
                       (plan_id, data_solicitud.get('id_servicio')))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Plan dado de alta correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se ha guardado los cambios'}), 404
    except Exception as e:
        print(f"Error al crear plan: {e}")
        return jsonify({'mensaje': 'Se produjo un error al dar de alta el plan'}), 500
    
@post_plan_bp.route('/bancario/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200