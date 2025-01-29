const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/api", // Ruta base para las solicitudes que quieres redirigir
    createProxyMiddleware({
      target: "http://127.0.0.1:1009", // Servidor de la API
      changeOrigin: true,
      pathRewrite: {
        "^/api": "", // Elimina el prefijo /api de la URL
      },
    })
  );
};
