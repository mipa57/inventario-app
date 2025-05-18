
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS inventario;
USE inventario;

-- Crear tabla productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(20) UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) DEFAULT 0.00
);

-- Insertar productos
INSERT INTO productos (id, codigo, nombre, cantidad, precio_unitario) VALUES
(2, 'P001', 'martillo', 50, 12.50),
(3, 'P002', 'Laptop Hp', 5, 800.00),
(8, 'P003', 'cemento', 100, 25.00),
(9, 'P004', 'clavos', 7855, 0.10),
(10, 'P005', 'serrucho', 1, 30.00);

-- Ejemplos de actualización y eliminación
-- UPDATE productos SET cantidad = 60 WHERE codigo = 'P001'; -- actualizar
-- DELETE FROM productos WHERE codigo = 'P005'; -- eliminar
