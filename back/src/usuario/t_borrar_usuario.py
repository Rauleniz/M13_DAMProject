from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from auth import verificar_credenciales_decorador
from models import Usuario
from back import db

borrar_usuario_bp = Blueprint('borrar_usuario', __name__)

@borrar_usuario_bp.route('/usuario_borrar', methods=['DELETE'])
@verificar_credenciales_decorador
def borrar_usuario(usuario):

    try:
        usuario_a_borrar = Usuario.query.get(usuario['id'])

        if not usuario_a_borrar:
            return jsonify({"message": "Usuario no encontrado"}), 404
        
        db.session.delete(usuario_a_borrar)
        db.session.commit()

        return jsonify({"message": "Cuenta eliminada correctamente"}), 200
    
    except Exception as e:
        # Manejo de errores
        return jsonify({'mensaje': 'Error al eliminar la cuenta', 'error': str(e)}), 500
