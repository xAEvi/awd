import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    correo_electronico: "",
    contraseña: "",
  });
  const [vehicles, setVehicles] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(
    !!sessionStorage.getItem("tokenapp")
  );
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const response = await axios.post(
        "http://127.0.0.1:1008/user/login",
        formData
      );
      const tokenapp = response.data.data["token"];
      console.log("Token:", tokenapp);
      sessionStorage.setItem("tokenapp", tokenapp);
      setIsLoggedIn(true);
    } catch (error) {
      console.error("Error durante el login:", error);
      setError("Credenciales incorrectas. Por favor, intenta de nuevo.");
    }
  };

  const fetchVehicles = async () => {
    setLoading(true);
    try {
      const tokenapp = sessionStorage.getItem("tokenapp");
      const response = await axios.get("/api/vehicles", {
        headers: {
          tokenapp: tokenapp,
        },
      });
      setVehicles(response.data.data);
      console.log(response.data.data);
    } catch (error) {
      console.error("Error obteniendo vehículos:", error);
      setError("Error al cargar los vehículos");
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    sessionStorage.removeItem("tokenapp");
    setIsLoggedIn(false);
    setVehicles([]);
  };

  useEffect(() => {
    if (isLoggedIn) {
      fetchVehicles();
    }
  }, [isLoggedIn]);

  if (!isLoggedIn) {
    return (
      <div className="App">
        <h1>Login</h1>
        {error && <p className="error">{error}</p>}
        <form onSubmit={handleSubmit}>
          <div>
            <label>Correo Electrónico:</label>
            <input
              type="email"
              name="correo_electronico"
              value={formData.correo_electronico}
              onChange={handleChange}
              required
            />
          </div>
          <div>
            <label>Contraseña:</label>
            <input
              type="password"
              name="contraseña"
              value={formData.contraseña}
              onChange={handleChange}
              required
            />
          </div>
          <button type="submit">Iniciar Sesión</button>
        </form>
      </div>
    );
  }

  return (
    <div className="App">
      <h1>Lista de Vehículos</h1>
      <button onClick={handleLogout} className="logout-button">
        Cerrar Sesión
      </button>

      {loading && <p>Cargando vehículos...</p>}
      {error && <p className="error">{error}</p>}

      {vehicles.length > 0 ? (
        <table>
          <thead>
            <tr>
              <th>Marca</th>
              <th>Modelo</th>
              <th>Año</th>
              <th>Color</th>
            </tr>
          </thead>
          <tbody>
            {vehicles.map((vehicle) => (
              <tr key={vehicle.id}>
                <td>{vehicle.marca}</td>
                <td>{vehicle.modelo}</td>
                <td>{vehicle.descripcion}</td>
                <td>{vehicle.placa}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        !loading && <p>No se encontraron vehículos</p>
      )}
    </div>
  );
}

export default App;
