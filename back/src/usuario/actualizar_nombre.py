from flask import Blueprint, request, jsonify

# Importar aquí las funciones necesarias para acceder a la base de datos y actualizar el nombre del usuario

actualizar_nombre_bp = Blueprint('actualizar_nombre', __name__)

@actualizar_nombre_bp.route('/usuario/actualizar/nombre', methods=['PATCH'])
def actualizar_nombre():
    try:
        # Obtener el nuevo nombre del usuario del cuerpo de la solicitud
        nuevo_nombre = request.json.get('nombre')

        # Aquí va el código para actualizar el nombre del usuario en la base de datos
        # Supongamos que hay una función actualizar_nombre_en_db(nombre)

        # Ejemplo de cómo se podría llamar a la función para actualizar el nombre en la base de datos
        # actualizar_nombre_en_db(nuevo_nombre)

        # Respuesta de éxito
        return jsonify({'mensaje': 'Nombre actualizado correctamente'}), 200
    except Exception as e:
        # Manejo de errores
        return jsonify({'mensaje': 'Error al actualizar el nombre', 'error': str(e)}), 500
