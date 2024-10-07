from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/datos', methods=["POST"])
def datos():
    usuario = request.form.get("usuario")
    contrasenia = request.form.get("contrasenia")
    try:
        db = MySQLdb.connect("192.168.0.27", usuario, contrasenia, "prueba")
        sql="SHOW TABLES"
        cursor = db.cursor()
        cursor.execute(sql)
        tablas = cursor.fetchall()

        return render_template('datos.html',tablas=tablas,conexion="bien")
    except MySQLdb.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return render_template('datos.html', conexion="mal")

if __name__ == '__main__':
    app.run(debug=True)
