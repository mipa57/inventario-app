# pruebas.py - Verifica conexión a MySQL de forma segura y clara

import mysql.connector
import os

# Configuración de conexión a MySQL con variables opcionales
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",

    "password": os.getenv("DB_PASSWORD", "Admin123456"),  # Usa variable de entorno o valor por defecto
    "database": "inventario"
}

try:
    db = mysql.connector.connect(**MYSQL_CONFIG)
    print(f"✅ Conexión exitosa a MySQL en la base de datos '{MYSQL_CONFIG['database']}'")

    # Opcional: cerrar la conexión inmediatamente si solo se verifica acceso
    db.close()

except mysql.connector.Error as err:
    print("❌ Error de conexión:", err)
    print("🔐 Asegúrate de que MySQL esté encendido y la base de datos exista.")

