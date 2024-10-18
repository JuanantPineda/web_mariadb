from flask import Flask, render_template, request
import MySQLdb

db = None  # Definir db como global

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/datos', methods=["POST"])
def datos():
    usuario = request.form.get("usuario")
    contrasenia = request.form.get("contrasenia")
    basedatos = request.form.get("basedatos")
    try:
        global db 
        db = MySQLdb.connect("192.168.0.29", usuario, contrasenia, basedatos)

        sql="SHOW TABLES"
        cursor = db.cursor()
        cursor.execute(sql)
        tablas = cursor.fetchall()

        return render_template('datos.html',tablas=tablas,conexion="bien")
    except MySQLdb.Error as e:
        return render_template('datos.html', conexion="mal")

@app.route('/tablas/<tabla>')
def detalle(tabla):
    try:
        cursor = db.cursor()
        cursor.execute(f"SHOW COLUMNS FROM {tabla}")
        columnas = cursor.fetchall()

        cursor.execute(f"SELECT * FROM {tabla}")
        filas = cursor.fetchall()

        return render_template('tablas.html', tabla=tabla, columnas=columnas, filas=filas)
    except MySQLdb.Error as e:
        return f"Error en la conexión: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
