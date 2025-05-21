# 🧾 Sistema de Inventario con Flask + MySQL

Este proyecto es una aplicación web sencilla para gestionar inventario (agregar, actualizar, eliminar y ver productos), desarrollada con **Flask** y conectada a **MySQL**. 

Incluye un diseño visual con **Bootstrap** y alertas dinámicas. Se puede ejecutar localmente con facilidad.

---

## 🚀 Requisitos para ejecutar la app

### 🔧 Programas necesarios:

- Python 3.10 o superior
- MySQL Server (ej: XAMPP, WAMP, Workbench, etc.)
- Git (opcional, pero recomendado)
- Navegador (Chrome, Edge, Firefox...)

---

## 📥 Instalación paso a paso

### 1. Clona o descarga el repositorio:

```
git clone https://github.com/mipa57/inventario-app.git
cd inventario-app
```

O descarga el ZIP y descomprímelo.

### 2. Configura la base de datos

- Abre MySQL Workbench o tu cliente favorito.
- Ejecuta el archivo `inventario.sql` para crear la base de datos y tabla.

---

### 3. Configura las variables de entorno

Edita el archivo `.env` y coloca la contraseña de tu MySQL:

```
MYSQL_PASSWORD=TuContraseñaDeMySQL
```

---

### 4. Activa el entorno virtual

En PowerShell (desde la carpeta del proyecto):

```powershell
.\venv\Scripts\Activate.ps1
```

> Si da error, ejecuta esto una vez como administrador:
>
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

### 5. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la aplicación

### Opción 1: Manual

```bash
python app.py
```

Y abre tu navegador en:

```
http://127.0.0.1:5000
```

---

### Opción 2: Usar archivo `iniciar.bat`

Haz doble clic sobre `iniciar.bat`. Este archivo:

- Activa el entorno virtual
- Abre Visual Studio Code (si está instalado)
- Abre una terminal con la app corriendo

---

## ✨ Funcionalidades

- ✅ Agregar productos (con código único)
- 🔄 Actualizar productos existentes (nombre y cantidad)
- 🗑️ Eliminar productos por código
- 📋 Ver todo el inventario
- ⚠️ Alertas visuales para éxito, error y duplicados
- 🎨 Estilo moderno con Bootstrap y gradientes

---

## 📦 Estructura del Proyecto

```
inventario-app/
├── app.py                  # App principal Flask
├── iniciar.bat            # Script para lanzar la app
├── iniciar_simple.bat     # Alternativa rápida sin abrir VSCode
├── requirements.txt       # Librerías necesarias
├── .env                   # Variables de entorno
├── inventario.sql         # Script de base de datos
├── templates/             # HTML con Jinja2
│   ├── index.html
│   └── inventario.html
├── static/css/style.css   # Estilos visuales
└── venv/                  # Entorno virtual (no se sube a GitHub)
```

---

## 📌 Créditos

- Desarrollado por **Miguel Bejarano**
- Proyecto educativo con Flask y MySQL

---

¿Problemas al ejecutar? Verifica:
- Que MySQL esté encendido
- Que el archivo `.env` tenga la contraseña correcta
- Que activaste el entorno virtual

¡Gracias por usar el sistema! 🎉
