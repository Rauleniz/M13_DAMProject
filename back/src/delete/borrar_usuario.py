
from flask import Blueprint, jsonify
from back.db import get_database_connection

delete_usuarios_bp = Blueprint('usuarios_delete', __name__)



@delete_usuarios_bp.route('/usuario/<int:id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM usuario WHERE id = %s", (id_usuario,))      
            connection.commit()

            if cursor.rowcount > 0:               
                return jsonify({'mensaje': 'Usuario cancelado'}), 200
            else:
                return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al eliminar usuario'}), 500

        
