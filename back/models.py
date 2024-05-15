from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellidos = db.Column(db.String(255))
    email = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    estatus = db.Column(db.String(255))
    img_perfil = db.Column(db.String(255))
    cancion = db.Column(db.String(255))
    id_plan = db.Column(db.Integer)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "email": self.email,
            "direccion": self.direccion,
            "estatus": self.estatus,
            "img_perfil": self.img_perfil,
            "cancion": self.cancion,
            "idPlan": self.id_plan,
            "username": self.username,
            "password": self.password
        }

class Conversacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario1 = db.Column(db.Integer)
    id_usuario2 = db.Column(db.Integer)
    ultima_actividad = db.Column(db.TIMESTAMP)

    def to_json(self):
        return {
            "id": self.id,
            "idUsuario1": self.id_usuario1,
            "idUsuario2": self.id_usuario2,
            "ultimaActividad": self.ultima_actividad
        }

class Mensaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_conversacion = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    contenido = db.Column(db.String(255))
    fecha_envio = db.Column(db.TIMESTAMP)

    def to_json(self):
        return {
            "id": self.id,
            "idConversacion": self.id_conversacion,
            "idUsuario": self.id_usuario,
            "contenido": self.contenido,
            "fechaEnvio": self.fecha_envio
        }

class DatosBancarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_factura = db.Column(db.Integer)
    nombre_iban = db.Column(db.String(255))
    numero_tarjeta = db.Column(db.String(255))
    caducidad_tarjeta = db.Column(db.String(255))
    cvc = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "idUsuario": self.id_usuario,
            "idFactura": self.id_factura,
            "nombreIban": self.nombre_iban,
            "numeroTarjeta": self.numero_tarjeta,
            "caducidadTarjeta": self.caducidad_tarjeta,
            "cvc": self.cvc
        }

class Multimedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    img = db.Column(db.String(255))
    song = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "idUsuario": self.id_usuario,
            "img": self.img,
            "song": self.song
        }


class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_plan = db.Column(db.Integer)
    fecha_servicio = db.Column(db.String(255))
    fecha_emision = db.Column(db.TIMESTAMP)
    token_ahorro = db.Column(db.Float)
    documentos = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "idUsuario": self.id_usuario,
            "idPlan": self.id_plan,
            "fechaServicio": self.fecha_servicio,
            "tokenAhorro": self.token_ahorro,
            "documentos": self.documentos
        }

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    cambio_plan = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cambioPlan": self.cambio_plan
        }


class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asignacion_tecnico = db.Column(db.String(255))
    cheque = db.Column(db.String(255))
    financiacion = db.Column(db.String(255))
    seguro = db.Column(db.String(255))
    alquiler_furgon = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "asignacionTecnico": self.asignacion_tecnico,
            "cheque": self.cheque,
            "financiacion": self.financiacion,
            "seguro": self.seguro,
            "alquilerFurgon": self.alquiler_furgon
        }

class PlanServicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_plan = db.Column(db.Integer)
    id_servicio = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "idPlan": self.id_plan,
            "idServicio": self.id_servicio
        }

class Ubicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    descripcion = db.Column(db.String(255))
    link1 = db.Column(db.String(255))
    link2 = db.Column(db.String(255))
    link3 = db.Column(db.String(255))
    link4 = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "idUsuario": self.id_usuario,
            "lat": self.lat,
            "lng": self.lng,
            "descripcion": self.descripcion,
            "link1": self.link1,
            "link2": self.link2,
            "link3": self.link3,
            "link4": self.link4
        }
    


    # OPCIÓN: @staticmethod coger varios diccionarios como argumentos y los combina en un solo diccionario.
    @staticmethod
    def combine_to_dict(*args):
        result = {}
        for model_dict in args:
            result.update(model_dict)
        return result
    
    # ASÍ SE UTILIZA el @staticmethod con tablas relacionadas:
    # usuarios_dict = usuario.to_dict()
    # multimedia_dict = multimedia.to_dict()
    # # Combina los diccionarios
    # resultado = Multimedia.combine_to_dict(usuarios_dict, multimedia_dict)



# Intentar inicializar la base de datos
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()