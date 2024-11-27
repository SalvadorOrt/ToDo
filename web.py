from flask import Flask, request, render_template, redirect, url_for
import pyodbc as sql
from tarea import Tarea

cadena_conexion = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-9NIFOJB;DATABASE=ToDo;Trusted_Connection=yes;'

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def root():
    conexion = sql.connect(cadena_conexion)
    cursor = conexion.cursor()
    tarea = Tarea()
    registros = cursor.execute(tarea.listarTarea()).fetchall()
    if request.method == 'POST':
        if "completar" in request.form:
            id_tarea = request.form.get("id_tarea")
            cursor.execute(*tarea.completarTarea(id_tarea))
            conexion.commit()  # Asegúrate de hacer commit para guardar los cambios en la base de datos
            return redirect(url_for('root'))
    return render_template('inicio.html', registros=registros)



@app.route('/insert',methods = ['POST','GET'])
def insertar():
    if request.method == 'POST':
        conexion = sql.connect(cadena_conexion)
        cursor = conexion.cursor()
        tarea = Tarea(request.form["desc"])
        cursor.execute(*tarea.insertarTarea())
        conexion.commit()
        conexion.close()
        return redirect(url_for('root'))
    return render_template('insertar_tarea.html')


@app.route('/edit/<int:id>',methods = ['POST','GET'])
def edit(id):
   if request.method == 'POST':
       conexion = sql.connect(cadena_conexion)
       cursor = conexion.cursor()
       if "actualizar" in request.form:
            tarea = Tarea()
            descripcion = str(request.form["descREC"])
            cursor.execute(*tarea.actualizarTarea(id,descripcion))
            conexion.commit()
            conexion.close()
            return redirect(url_for('root'))
       if "eliminar" in request.form:
            tarea = Tarea()
            cursor.execute(*tarea.eliminarTarea(id))
            conexion.commit()
            conexion.close()
            return redirect(url_for('root'))
       


   if request.method == 'GET':
        conexion = sql.connect(cadena_conexion)
        cursor = conexion.cursor()
        tarea = Tarea()
        registro = cursor.execute(*tarea.obternerTarea_ID(id)).fetchone()
        conexion.close()
        return render_template('editar.html',registro = registro)
   

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0',port = '5000')
