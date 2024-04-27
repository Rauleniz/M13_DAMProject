# from flask import Flask, request, jsonify
# import mysql.connector
# from db import conectar_mysql

# app = Flask(__name__)


# conexion = conectar_mysql()

# # Función para obtener los datos de un usuario desde la base de datos MySQL
# def obtener_datos_usuario(id_usuario):
#     try:
#         if conexion:
#             try:
#                 cursor = conexion.cursor(dictionary=True)
#                 consulta = "SELECT * FROM usuario WHERE id = %s"
#                 cursor.execute(consulta, (id_usuario,))
#                 usuario = cursor.fetchone()
#                 return usuario
#             except mysql.connector.Error as error:
#                 print("Error al obtener los datos del usuario:", error)
#             finally:
#                 if conexion.is_connected():
#                     cursor.close()
#                     conexion.close()
#     except mysql.connector.Error as error:
#         print("Error al obtener los datos del usuario:", error)


# # Endpoint para obtener los datos actuales del usuario
# @app.route('/usuario', methods=['GET'])
# def obtener_usuario():
#     # Aquí obtienes el ID del usuario de alguna manera, por ejemplo, desde un token de autenticación
#     id_usuario = obtener_id_usuario_desde_token(request.headers.get('Authorization'))
#     # Luego, obtienes los datos del usuario usando la función definida anteriormente
#     datos_usuario = obtener_datos_usuario(id_usuario)
#     return jsonify(datos_usuario)

# # Endpoint para actualizar los datos del usuario
# @app.route('/usuario', methods=['PUT'])
# def actualizar_usuario():
#     datos_actualizados = request.json
#     # Aquí realizas la lógica para actualizar los datos del usuario en la base de datos
#     # Esto implicaría ejecutar una consulta UPDATE en la base de datos MySQL
#     # Por simplicidad, aquí solo se devuelve un mensaje de éxito
#     return jsonify({'mensaje': 'Datos del usuario actualizados correctamente'})

# if __name__ == '__main__':
#     app.run(debug=True)
