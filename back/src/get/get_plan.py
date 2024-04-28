# En usuarios.py

from flask import Blueprint, jsonify
from back.db import get_database_connection

get_plan_bp = Blueprint('plan_get', __name__)

# planes = []

# @get_plan_bp.route('/plan', methods=['GET'])
# def obtener_planes():

#     return jsonify(planes)

@get_plan_bp.route('/plan/<int:id_plan>', methods=['GET'])
def obtener_plan(id_plan):
    connection = get_database_connection()
    try:
        cursor = connection.cursor() 
        cursor.execute("SELECT * FROM plan WHERE id = %s", (id_plan, ))
        plan = cursor.fetchone()  
        if plan:
            return jsonify(plan)
        else:
            return jsonify({'mensaje': 'Plan no encontrado'}), 404
    
    except Exception as e:
        print(f"Error al obtener plan: {e}")
        return jsonify({'mensaje': 'Se produjo un error al obtener plan'}), 500

        
