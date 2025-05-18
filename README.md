# 📦 Sistema de Gestión de Inventario

Aplicación web desarrollada con **Flask + MySQL**, diseñada para registrar, actualizar, eliminar productos y visualizar el inventario completo en tiempo real.

---

## 🚀 Características

* Agregar productos con nombre y cantidad.
* Evita duplicados: si el producto existe, actualiza la cantidad.
* Mostrar inventario completo en otra vista.
* Eliminar productos.
* Actualizar cantidad de stock.
* Diseño moderno con **Bootstrap 5** y alertas visuales.
* Base de datos en **MySQL**.
* Interfaz dividida en dos ventanas (Inicio + Inventario).

---

## 💠 Tecnologías utilizadas

* Python 3.11+
* Flask
* MySQL
* HTML5, CSS3
* Bootstrap 5
* Git / GitHub

---

## ⚙️ Instalación y uso

### 1. Clona el repositorio

```bash
git clone https://github.com/mipa57/inventario-app.git
cd inventario-app
```

### 2. Crea y activa un entorno virtual

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

### 3. Instala las dependencias

```bash
pip install flask mysql-connector-python python-dotenv
```

### 4. Configura tu archivo `.env`

Crea un archivo `.env` con:

```env
MYSQL_PASSWORD=tu_contraseña_mysql
```

### 5. Ejecuta la aplicación

```bash
python app.py
```

---

## 📃 Estructura del proyecto

```
inventario-app/
|
|├── app.py                # Código principal de Flask
|├── templates/            # Vistas HTML (inicio + inventario)
|├── static/style.css      # Estilos personalizados
|├── .env                  # Contraseña segura para MySQL (no se sube)
|├── .gitignore            # Archivos ignorados
|├── requirements.txt      # Dependencias del proyecto (pendiente)
└── README.md             # Este archivo
```

---

## 📊 Capturas (opcional)

Puedes incluir capturas de pantalla de las dos vistas principales con:

```markdown
![Inicio](ruta/imagen1.png)
![Inventario](ruta/imagen2.png)
```

---

## 📌 Autor

Desarrollado por **Miguel Bejarano** — [LinkedIn](https://www.linkedin.com/in/tu_usuario/)
Colombia 🇨🇴
