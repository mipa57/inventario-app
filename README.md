# Sistema de Inventario Web con Flask y MySQL

Este proyecto es una aplicación web de inventario creada con **Flask**, **MySQL** y **Bootstrap**. Permite agregar, actualizar, eliminar productos y visualizar el inventario completo.

---

## 🌐 Demo en Producción (Frontend Estático)

Puedes ver la versión estática del frontend en:

➡ [https://inventariofrontend.netlify.app](https://inventariofrontend.netlify.app)

---

## 📄 Requisitos

* Python 3.10 o superior
* MySQL Server (activo y funcionando)
* Git (opcional, para clonar el repo)

---

## 📝 Instalación Local

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
pip install -r requirements.txt
```

### 4. Crea la base de datos en MySQL

Desde tu consola de MySQL ejecuta:

```sql
SOURCE inventario.sql;
```

### 5. Configura el archivo `.env`

Crea un archivo `.env` con tu contraseña de MySQL:

```
MYSQL_PASSWORD=tu_contraseña_aqui
```

### 6. Inicia la aplicación

Puedes usar:

```bash
python app.py
```

O si prefieres, ejecuta `iniciar.bat` o `iniciar_simple.bat`.

Abre tu navegador en [http://localhost:5000](http://localhost:5000)

---

## 🔄 Características

* Agregar productos (con código, nombre, cantidad)
* Actualizar datos de productos existentes
* Eliminar productos
* Ver el inventario completo (tabla)
* Alertas visuales para éxito, advertencia o error
* Validaciones simples (productos duplicados)
* Interfaz estilizada con Bootstrap 5

---

## 📅 Estructura del Proyecto

```
inventario-app/
├── app.py                 # Lógica principal de la aplicación
├── templates/             # Vistas HTML (index.html, inventario.html)
├── static/css/style.css   # Estilos personalizados
├── .env                   # Contraseña de MySQL (ignorado por Git)
├── .gitignore             # Archivos ignorados
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Este archivo
├── inventario.sql         # Script para crear la base de datos y tabla
├── iniciar.bat            # Script para lanzar el servidor y VS Code
├── iniciar_simple.bat     # Alternativa sin abrir VS Code
├── pruebas.py             # Verifica conexión MySQL
```

---

## 🎓 Autor

**Miguel Gustavo Bejarano Patiño**
[Portafolio](https://portafolio-desarrollador.netlify.app)
[GitHub](https://github.com/mipa57)

---

## 🎉 Licencia

Este proyecto es de libre uso educativo. Puedes adaptarlo, mejorarlo y compartirlo bajo tu propio repositorio. ¡Se agradecen estrellas! ✨
