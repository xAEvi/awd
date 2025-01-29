CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo_electronico VARCHAR(255) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,  -- Usar hashing seguro en producción
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('administrador', 'invitado'))
);

CREATE TABLE vehiculos (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(255) NOT NULL,
    modelo VARCHAR(255) NOT NULL,
    año INTEGER NOT NULL,
    placa VARCHAR(10) UNIQUE NOT NULL,
    descripcion TEXT
);

INSERT INTO usuarios (nombre, correo_electronico, contrasena, rol) VALUES
('Juan Pérez', 'juan.perez@example.com', '$2b$12$9fK5yCEb9oVxO/JFXrLnOefC012jMlS91SDxN63Pab6gQvKOxJrVy', 'administrador'),
('Ana García', 'ana.garcia@example.com', 'contraseña_segura_2', 'invitado');

INSERT INTO vehiculos (marca, modelo, año, placa, descripcion) VALUES
('Toyota', 'Corolla', 2022, 'ABC-123', 'Sedan familiar'),
('Honda', 'Civic', 2023, 'DEF-456', 'Auto deportivo'),
('Ford', 'F-150', 2021, 'GHI-789', 'Camioneta'),
('Chevrolet', 'Silverado', 2020, 'JKL-012', 'Camioneta grande'),
('Nissan', 'Sentra', 2022, 'MNO-345', 'Sedan compacto'),
('Hyundai', 'Tucson', 2023, 'PQR-678', 'SUV'),
('Kia', 'Sportage', 2021, 'STU-901', 'SUV compacto'),
('Mazda', 'CX-5', 2020, 'VWX-234', 'SUV mediana'),
('Subaru', 'Outback', 2022, 'YZ-567', 'Wagon'),
('BMW', 'X5', 2023, 'AAA-111', 'SUV de lujo');