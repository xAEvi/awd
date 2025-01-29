from flask import request
from flask_restful import Resource
from ..Components.get_vehicles import VehicleComponent # Importa el componente correcto
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success
from ...api.Components.jwt_component import JWTComponent

class GetVehiclesService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log('Servicio de obtención de vehículos ejecutando')

            # Obtener el token desde los headers
            token = request.headers.get('tokenapp')
            if not token:
                return response_error('Token no proporcionado')

            # Validar el token
            if not JWTComponent.token_validate(token):
                return response_error('Token no válido')

            # Llamar al componente para obtener los vehículos
            result_get_vehicles = VehicleComponent.get_all_vehicles()

            # Si la consulta fue exitosa, devolver los vehículos
            if result_get_vehicles['result']:
                return response_success(result_get_vehicles['data'])
            else:
                return response_error(result_get_vehicles['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error('Error en el servicio -> ' + str(err))