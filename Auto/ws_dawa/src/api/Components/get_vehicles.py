from ...utils.general.logs import HandleLogs
from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.response import internal_response

class VehicleComponent:
    @staticmethod
    def get_all_vehicles():
        try:
            result = False
            message = None
            data = None

            # SQL para obtener todos los vehículos
            sql = """
            SELECT id, marca, modelo, año, placa, descripcion
            FROM vehiculos;
            """

            # Ejecutar la consulta.  Se asume que getRecords retorna un diccionario.
            query_result = DataBaseHandle.getRecords(sql, 0)

            if query_result['result']:
                data = query_result['data']
                result = True
                message = 'Vehículos obtenidos exitosamente'
            else:
                message = 'Error al obtener los vehículos: ' + query_result['message']
                HandleLogs.write_log('Error al ejecutar la consulta para obtener vehículos -> ' + query_result['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            message = 'Error al obtener los vehículos -> ' + str(err)
        finally:
            return internal_response(result, data, message)