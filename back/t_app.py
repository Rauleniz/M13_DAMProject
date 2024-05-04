import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from endpoints import register_endpoints
from auth import auth_bp


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

rutas = ["http://localhost:5500", "http://127.0.0.1:5500"]

app = Flask(__name__)
CORS(app, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], resources={r"/*": {"origins": rutas}}, methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])

app.config['CORS_LOGGING'] = True
app.config['SECRET_KEY'] = 'DamM13&Proj3ct'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/m13db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Registrar blueprints de los endpoints
register_endpoints(app)

# Registrar el blueprint de autenticación
app.register_blueprint(auth_bp)

# 01/05 - VALORAR SI HACER TODOS LOS ENDPOINTS EN EL APP.PY
@app.route('/')
def index():      
    print (f'Vamosssssss')
    return f'exitooooo'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
