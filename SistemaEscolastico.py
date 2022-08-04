from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_session import Session
from funcionesAyuda import login_requerido, admin_requerido, docente_requerido, estudiante_requerido
from validacion import validarUsuario, validarTipoUsuario

# Configurar app
app = Flask(__name__)
# Por seguridad necesita esto aleatorio
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Configurar sesion (cookies para reconocer usuario)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Pantalla Principal del usuario 
# REQ002 dirigir al usuario a su interfaz debida
@app.route("/")
@login_requerido
def index():
    if session.get("usertype") == 'administrador':
        return render_template("menu_administrador.html")
    
    if session.get("usertype") == 'docente':
        return render_template("menu_docente.html")
    
    if session.get("usertype") == 'estudiante':
        flash("Perdon ESTUDIANTE, pronto lo arreglaremos")
        return redirect(url_for('error404'))
    
    return redirect(url_for("error404"))

# Login
@app.route("/login", methods=['GET','POST']) # Get: Login vacio - Post: Form llenado 
def login():
    error = None

    #Revisar si ya esta iniciado sesion
    if session.get("username"):
        return redirect("/")

    # Si el usuario aplasto enviar
    if request.method == 'POST':
        # Extraer variables del form
        username = request.form['username']
        contrasena = request.form['contrasena']

        # Si los datos no coinciden con BD
        if not validarUsuario(username, contrasena):
            error = "Datos erróneos de Login"
        # Inicio correcto y tipo de Usuario
        else:
            tipoUsuario = validarTipoUsuario(username)

            # Recordar usuario en sesion
            session["username"] = username
            session["usertype"] = tipoUsuario

            return redirect("/") # Pendiente de desarrollar

    # Si no se inicio sesion correctamnete, regresar al login con el error debido
    return render_template('login.html', error=error)

# Funciones de Admin
@app.route("/registrar-docente")
@admin_requerido
def registrar_docente():
    return render_template("registro-docente.html")

@app.route("/registrar-estudiante")
@admin_requerido
def registrar_estudiante():
    return render_template("registro-estudiante.html")

@app.route("/registrar-asignatura-paralelo")
@admin_requerido
def registrar_asignatura_paralelo():
    return render_template("registro-asignatura-paralelo.html")

@app.route("/registrar-matricula")
@admin_requerido
def registrar_matricula():
    return render_template("registro-matricula.html")

# Funciones de Estudiante
@app.route("/registrar-notas")
@docente_requerido
def registrar_notas():
    return render_template("registro-notas.html")

@app.route("/reporte-notas")
@docente_requerido
def reporte_notas():
    return render_template("reporte-notas.html")

# Logout
@app.route("/logout")
def logout():
    session["username"] = None
    session["usertype"] = None
    return redirect("/login")

# Error
@app.route("/404")
def error404():
    return render_template("404.html")
