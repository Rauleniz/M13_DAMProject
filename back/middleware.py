

# from flask import Flask
# #from flask_cors import CORS

# app = Flask(__name__)
# #CORS(app, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], resources={r"/*": {"origins": ["http://localhost:5500", "http://127.0.0.1:5500"]}}, methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])


# # Middleware para manejar CORS
# @app.after_request
# def add_cors_headers(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'  # Permite solicitudes desde cualquier origen
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'  # Especifica los encabezados permitidos
#     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE'  # Especifica los métodos permitidos
#     return response

