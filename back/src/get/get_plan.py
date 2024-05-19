# En usuarios.py

from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

get_plan_bp = Blueprint('plan_get', __name__)


@get_plan_bp.route('/plan/<int:usuario_id>', methods=['GET'])
def obtener_plan(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']

        connection = get_database_connection()
        cursor = connection.cursor() 
        cursor.execute("SELECT plan.nombre FROM plan INNER JOIN usuario ON usuario.id_plan = plan.id WHERE usuario.id = %s", (usuario_id, ))
        plan = cursor.fetchone()  
        if plan:
            return jsonify(plan)
        else:
            return jsonify({'mensaje': 'Plan no encontrado'}), 404
    
    except Exception as e:
        print(f"Error al obtener plan: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener plan'}), 500

        
@get_plan_bp.route('/plan/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200