# En endpoints.py
from flask import jsonify
from app import app
from models import Usuario, Conversacion, Mensaje, DatosBancarios, Multimedia, Factura, Plan, Servicio, PlanServicio, Ubicacion


@app.route('/datos_completos', methods=['GET'])
def obtener_datos_completos():
    # Obtener datos de las diferentes tablas
    usuarios = Usuario.query.all()
    conversaciones = Conversacion.query.all()
    mensajes = Mensaje.query.all()
    datos_bancarios = DatosBancarios.query.all()
    multimedia = Multimedia.query.all()
    factura = Factura.query.all()
    plan = Plan.query.all()
    servicio = Servicio.query.all()
    plan_servicio = PlanServicio.query.all()
    ubicacion = Ubicacion.query.all()


    # Convertir objetos de cada tabla en diccionarios
    usuarios_dict = [usuario.to_json() for usuario in usuarios]
    conversaciones_dict = [conversacion.to_json() for conversacion in conversaciones]
    mensajes_dict = [mensaje.to_json() for mensaje in mensajes]
    datos_bancarios_dict = [dato_bancario.to_json() for dato_bancario in datos_bancarios]
    multimedia_dict = [multimedia_item.to_json() for multimedia_item in multimedia]
    factura_dict = [factura_item.to_json() for factura_item in factura]
    plan_dict = [plan_item.to_json() for plan_item in plan]
    servicio_dict = [servicio_item.to_json() for servicio_item in servicio]
    plan_servicio_dict = [plan_servicio_item.to_json() for plan_servicio_item in plan_servicio]
    ubicacion_dict = [ubicacion_item.to_json() for ubicacion_item in ubicacion]

    # Combinar todos los diccionarios en una lista
    datos_completos = {
        'usuarios': usuarios_dict,
        'conversaciones': conversaciones_dict,
        'mensajes': mensajes_dict,
        'datos_bancarios': datos_bancarios_dict,
        'multimedia': multimedia_dict,
        'factura': factura_dict,
        'plan_dict': plan_dict,
        'servicio_dict': servicio_dict,
        'plan_servicio_dict': plan_servicio_dict,
        'ubicacion_dict': ubicacion_dict
    }

    return jsonify(datos_completos)
