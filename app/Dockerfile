# Etapa de construcción
FROM node AS build

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY package.json package-lock.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos del proyecto
COPY . .

# Construye la aplicación
RUN npm run build

# Etapa de producción con Nginx
FROM nginx:alpine

# Elimina la configuración por defecto de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia los archivos construidos en la etapa anterior a la carpeta de Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expone el puerto 3000
EXPOSE 3000

# Comando por defecto para ejecutar Nginx
CMD ["nginx", "-g", "daemon off;"]
