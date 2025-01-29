import bcrypt
from ...utils.general.logs import HandleLogs
from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.response import internal_response
from .jwt_component import JWTComponent # Importar JWTComponent

class LoginComponent:
    @staticmethod
    def login_user(p_correo, p_contrasena):
        try:
            result = False
            message = None
            data = None

            sql = """
            SELECT id, nombre, contrasena, rol FROM usuarios WHERE correo_electronico = %s;
            """
            record = (p_correo,)

            query_result = DataBaseHandle.getRecords(sql, 1, record)

            if query_result['result']:
                if query_result['data']:
                    user = query_result['data']
                    if bcrypt.checkpw(p_contrasena.encode('utf-8'), user['contrasena'].encode('utf-8')):
                        # Generar el token JWT
                        token = JWTComponent.token_generate(user['nombre']) #Pasamos el nombre de usuario

                        if token: #Verificamos si el token se generó correctamente
                            result = True
                            message = 'Inicio de sesión exitoso'
                            data = {'id': user['id'], 'nombre': user['nombre'], 'rol': user['rol'], 'token': token}
                        else:
                            message = 'Error al generar el token'
                    else:
                        message = 'Contraseña incorrecta'
                else:
                    message = 'Usuario no encontrado'
            else:
                message = 'Error al iniciar sesión: ' + query_result['message']
                HandleLogs.write_log('Error al ejecutar login -> ' + query_result['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            message = 'Error al iniciar sesión -> ' + str(err)
        finally:
            return internal_response(result, data, message)