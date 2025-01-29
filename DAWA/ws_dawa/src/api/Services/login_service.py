from flask import request
from flask_restful import Resource
from ..Components.login_component import LoginComponent # Importa el componente de login
from ..Model.Request.login_request import LoginRequest # Importa el request de login
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success

class LoginService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log('Servicio de inicio de sesión ejecutando')

            rq_json = request.get_json()

            new_request = LoginRequest()
            errors = new_request.validate(rq_json)

            if errors:
                HandleLogs.write_log('Error al validar el Request ->' + str(errors))
                return response_error('Error al validar el Request ->' + str(errors))

            correo = rq_json['correo_electronico']
            contraseña = rq_json['contraseña']

            result_login = LoginComponent.login_user(correo, contraseña)

            if result_login['result']:
                return response_success(result_login['data'])
            else:
                return response_error(result_login['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error('Error en el servicio ->' + str(err))