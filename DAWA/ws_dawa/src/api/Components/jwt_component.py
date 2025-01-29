import jwt


from ...utils.general.config import Parametros
from ...utils.general.logs import HandleLogs

from datetime import datetime, timedelta
import pytz


class JWTComponent:
    @staticmethod
    def token_generate(p_user):
        try:
            respuesta = None

            timezone = pytz.timezone('America/Guayaquil')
            payload = {
                'iat': datetime.now(tz=timezone),
                'exp': datetime.now(tz=timezone) + timedelta(minutes=15),
                'username': p_user
            }

            respuesta = jwt.encode(payload, Parametros.secret_jwt, 'HS256')

        except Exception as err:
            HandleLogs.write_log('Ocurrió un error al generar el token para el usuario' + p_user)
            HandleLogs.write_error(err)
        finally:
            return respuesta

    @staticmethod
    def token_validate(p_token):
        try:
            respuesta = False

            resp_jwt = jwt.decode(p_token, Parametros.secret_jwt, algorithms=['HS256'])
            if resp_jwt is not None:
                respuesta = True


        except Exception as err:
            HandleLogs.write_log('Ocurrió un error al validar el token para el usuario' + p_token)
            HandleLogs.write_error(err)
        finally:
            return respuesta
