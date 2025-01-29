import bcrypt
from ...utils.general.logs import HandleLogs
from ...utils.database.connection_db import DataBaseHandle  # Usamos ExecuteNonQuery aquí
from ...utils.general.response import internal_response


class UserComponent:
    @staticmethod
    def create_user(p_nombre, p_correo, p_contrasena, p_rol): #Modificado para usar el rol
        try:
            result = False
            message = None
            data = None

            # Encriptar la contraseña
            hashed_password = bcrypt.hashpw(p_contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # SQL para insertar el usuario.  Ajustado a la tabla usuarios
            sql = """
            INSERT INTO usuarios (nombre, correo_electronico, contrasena, rol)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
            """
            record = (p_nombre, p_correo, hashed_password, p_rol)

            # Ejecutar el SQL usando ExecuteNonQuery
            insert_result = DataBaseHandle.ExecuteNonQuery(sql, record)

            if insert_result['result']:
                message = 'Usuario creado exitosamente'
                result = True
                data = {'nombre': p_nombre, 'correo_electronico': p_correo}
            else:
                message = 'Error al crear el usuario: ' + insert_result['message']
                HandleLogs.write_log('Error al ejecutar creación de usuario -> ' + insert_result['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            message = 'Error al crear el usuario -> ' + str(err)
        finally:
            return internal_response(result, data, message)