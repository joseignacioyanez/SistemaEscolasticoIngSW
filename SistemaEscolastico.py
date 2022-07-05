from flask import Flask, render_template, redirect, url_for, request, flash
from validacion import validarUsuario, validarTipoUsuario

app = Flask(__name__)
# Por seguridad necesita esto aleatorio
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Redirigir al Login
@app.route("/")
def index():    
    return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST']) # Get: Login vacio - Post: Form llenado 
def login():
    error = None

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
            mensaje = "Iniciaste sesión exitosamente " + username + "!" + " Tipo de Usuario: " + tipoUsuario
            flash(mensaje)
            return redirect(url_for('error404')) # Pendiente de desarrollar

    # Si no se inicio sesion correctamnete, regresar al login con el error debido
    return render_template('login.html', error=error)

@app.route("/404")
def error404():
    return render_template("404.html")