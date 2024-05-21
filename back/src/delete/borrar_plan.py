
from flask import Blueprint, jsonify
from back.db import get_database_connection

delete_plan_bp = Blueprint('plan_delete', __name__)



@delete_plan_bp.route('/plan/<int:id_usuario>', methods=['DELETE'])
def borrar_plan(id_plan):
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()            
            cursor.execute("DELETE FROM plan WHERE id = %s", (id_plan,))     
            connection.commit()

            if cursor.rowcount > 0:
                return jsonify({'mensaje': 'Plan eliminado'}), 200
            else:
                return jsonify({'mensaje': 'Plan no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener el plan: {e}")
        return jsonify({'mensaje': 'Se produjo un error al eliminar el plan'}), 500

        
