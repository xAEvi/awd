# create_user_service.py
from flask import request
from flask_restful import Resource
from ..Components.create_user_component import UserComponent # Importa el componente correcto
from ..Model.Request.user_request import CreateUserRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success

class CreateUserService(Resource): # Nombre de la clase corregido
    @staticmethod
    def post():
        try:
            HandleLogs.write_log('Servicio de creación de usuario Ejecutando')

            rq_json = request.get_json()

            # Accede a los datos validados a través del diccionario "data"
            nombre = rq_json['nombre']
            correo = rq_json['correo_electronico']
            contrasena = rq_json['contraseña']
            rol = rq_json['rol']

            result_create_user = UserComponent.create_user(nombre, correo, contrasena, rol)

            if result_create_user['result']:
                return response_success(result_create_user['data'])
            else:
                return response_error(result_create_user['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error('Error en el servicio ->' + err.__str__())