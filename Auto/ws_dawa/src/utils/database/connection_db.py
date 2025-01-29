#Permitir conectarme a una base de datos PostgreSQl
import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor

from ..general.config import Parametros
from ..general.logs import HandleLogs
from ..general.response import internal_response


def conn_db():
    return psycopg2.connect(host=Parametros.db_host,
                            port=int(Parametros.db_port),
                            user=Parametros.db_user,
                            password=Parametros.db_pass,
                            database=Parametros.db_name,
                            cursor_factory=RealDictCursor)

class DataBaseHandle:
    #Nuestros Metodos para ejecutar sentencias.
    #ejecuta metodos de tipo select
    @staticmethod
    def getRecords(query,  tamanio, record=()):
        try:
            result = False
            message = None
            data = None

            conn = conn_db()
            cursor = conn.cursor()
            if len(record) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, record)
            # tamanio es 0 todos, 1 solo uno, > 1 n registros
            if tamanio == 0:
                res = cursor.fetchall()
            elif tamanio == 1:
                res = cursor.fetchone()
            else:
                res = cursor.fetchmany(tamanio)

            data = res
            result = True
        except Exception as ex:
            HandleLogs.write_error(ex)
            message = ex.__str__()
        finally:
            cursor.close()
            conn.close()
            return internal_response(result, data, message)

    #ejecuta metodos de tipo INSERT-UPDATE-DELETE
    @staticmethod
    def ExecuteNonQuery(query, record):
        try:
            result = False
            message = None
            data = None
            conn = conn_db()
            cursor = conn.cursor()

            # Ejecutar la query con o sin parámetros
            if len(record) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, record)

            # Comprobar si el query es un INSERT
            if query.upper().find('INSERT') > -1:
                try:
                    cursor.execute('SELECT LASTVAL()')  # Obtener el último valor insertado
                    ult_id = cursor.fetchone()['lastval']
                    conn.commit()  # Confirmar la transacción
                    data = ult_id  # Retornar el id insertado
                except Exception as ex:
                    HandleLogs.write_error(ex)
                    message = "Error al ejecutar el INSERT"
                    data = 0
            # Comprobar si el query es un UPDATE
            elif query.upper().find('UPDATE') > -1:
                try:
                    conn.commit()  # Confirmar la transacción
                    data = cursor.rowcount  # Número de filas afectadas
                except Exception as ex:
                    HandleLogs.write_error(ex)
                    message = "Error al ejecutar el UPDATE"
                    data = 0
            # Comprobar si el query es un DELETE
            elif query.upper().find('DELETE') > -1:
                try:
                    conn.commit()  # Confirmar la transacción
                    data = cursor.rowcount  # Número de filas eliminadas
                except Exception as ex:
                    HandleLogs.write_error(ex)
                    message = "Error al ejecutar el DELETE"
                    data = 0
            else:
                # En caso de otros tipos de operaciones (selects, etc.)
                data = 0

            result = True
        except Exception as ex:
            HandleLogs.write_error(ex)
            message = ex.__str__()
        finally:
            cursor.close()
            conn.close()
            return internal_response(result, data, message)




