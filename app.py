from flask import Flask, render_template, request, redirect, flash
import mysql.connector
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

# Conexión a MySQL
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="inventario"
    )
    print("✅ Conexión exitosa a MySQL")
except mysql.connector.Error as err:
    print("❌ Error al conectar a MySQL:", err)
    exit()

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        codigo = request.form['codigo'].strip()
        nombre = request.form['nombre'].strip()
        cantidad = int(request.form['cantidad'])

        cursor = db.cursor()
        cursor.execute("SELECT id, cantidad FROM productos WHERE codigo = %s", (codigo,))
        existente = cursor.fetchone()

        if existente:
            nuevo_total = existente[1] + cantidad
            cursor.execute("UPDATE productos SET cantidad = %s WHERE id = %s", (nuevo_total, existente[0]))
            flash("🟡 Producto ya existente, cantidad actualizada.", "warning")
        else:
            cursor.execute("INSERT INTO productos (codigo, nombre, cantidad) VALUES (%s, %s, %s)", (codigo, nombre, cantidad))
            flash("✅ Producto agregado exitosamente.", "success")

        db.commit()
        cursor.close()

    cursor = db.cursor()
    cursor.execute("SELECT id, codigo, nombre, cantidad, precio_unitario FROM productos")
    productos = cursor.fetchall()
    cursor.close()

    return render_template('index.html', productos=productos)

@app.route('/actualizar', methods=['POST'])
def actualizar():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    cursor = db.cursor()
    cursor.execute("UPDATE productos SET nombre = %s, cantidad = %s WHERE codigo = %s", (nombre, cantidad, codigo))
    db.commit()
    cursor.close()
    flash("🔄 Producto actualizado correctamente.", "info")
    return redirect('/')

@app.route('/eliminar', methods=['POST'])
def eliminar():
    codigo = request.form['codigo']
    cursor = db.cursor()
    cursor.execute("DELETE FROM productos WHERE codigo = %s", (codigo,))
    db.commit()
    cursor.close()
    flash("🗑️ Producto eliminado correctamente.", "danger")
    return redirect('/')

@app.route('/inventario')
def ver_inventario():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()
    productos = []

    for fila in resultados:
        productos.append({
            'codigo': fila[1],
            'nombre': fila[2],
            'cantidad': fila[3],
            'precio_unitario': fila[4] if len(fila) > 4 else 'N/A'
        })

    cursor.close()
    return render_template('inventario.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
