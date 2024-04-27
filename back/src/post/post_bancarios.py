from flask import Blueprint, jsonify, request
from back.db import database

post_bancarios_bp = Blueprint('bancarios_post', __name__)

@post_bancarios_bp.route('/bancario', methods=['POST'])
def nuevo_datobancario():
    try:    
        data = request.json
        nombre_tarjeta = data.get('nombre_tarjeta')
        numero_tarjeta = data.get('numero_tarjeta')
        caducidad_tarjeta = data.get('caducidad_tarjeta')
        cvc = data.get('cvc')
  
        cursor = database.cursor()
        sql = "INSERT INTO datosbancarios (nombre_tarjeta, numero_tarjeta, caducidad_tarjeta, cvc) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre_tarjeta, numero_tarjeta, caducidad_tarjeta, cvc))
        database.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Datos Bancarios dados de alta correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se ha guardado los datos bancarios'}), 404
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return jsonify({'mensaje': 'Se produjo un error al dar de alta los datos bancarios'}), 500
