from flask import Blueprint, current_app, request, jsonify
from datetime import datetime

import jwt
from back.db import get_database_connection

crear_conversacion_bp = Blueprint('crear_conversacion', __name__)

@crear_conversacion_bp.route('/conversacion/<int:usuario_id>', methods=['POST'])
def crear_conversacion(usuario_id):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:       
        data = request.json
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])

        id_usuario1 = data.get('id_usuario1')
        id_usuario2 = data.get('id_usuario2')
        contenido = data.get('contenido')

        # Verificar si la conversación ya existe entre los usuarios
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM conversacion WHERE (id_usuario1 = %s AND id_usuario2 = %s) OR (id_usuario1 = %s AND id_usuario2 = %s)",
                       (id_usuario1, id_usuario2, id_usuario2, id_usuario1))
        conversacion_existente = cursor.fetchone()

        if conversacion_existente:
            id_conversacion = conversacion_existente[0]
        else:
            # Si la conversación no existe, crear una nueva
            cursor.execute("INSERT INTO conversacion (id_usuario1, id_usuario2) VALUES (%s, %s)",
                           (id_usuario1, id_usuario2))
            connection.commit()
            id_conversacion = cursor.lastrowid

        # Agregar el mensaje a la conversación
        cursor.execute("INSERT INTO mensaje (id_conversacion, id_usuario, contenido) VALUES (%s, %s, %s)",
                       (id_conversacion, id_usuario1, contenido))
        connection.commit()

        # Devolver la información de la conversación creada
        nueva_conversacion = {
            'id_conversacion': id_conversacion,
            'id_usuario1': id_usuario1,
            'id_usuario2': id_usuario2,
            'ultimo_mensaje': contenido
        }

        return jsonify(nueva_conversacion), 201

    except Exception as e:
        return jsonify({'mensaje': 'Error al crear la conversación', 'error': str(e)}), 500
