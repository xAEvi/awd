# Usa una imagen base oficial de Python
FROM python

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY ws_dawa/src/utils/requerimientos.txt /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requerimientos.txt

# Copia todo el directorio 'ws_dawa' al contenedor
COPY ws_dawa /app/

# Expone el puerto en el que el backend correrá (ajústalo según tu configuración)
EXPOSE 1009

# Comando para ejecutar el backend
CMD ["python", "app.py"]
