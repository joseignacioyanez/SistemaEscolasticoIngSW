from functools import wraps
from flask import session, redirect

# Funcion ayuda para Decorador que requiera Login
def login_requerido(f):
    """
    Decora rutas para requerir login.

    https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Funciones para verificar permisos

def admin_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("usertype") != 'administrador':
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def docente_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("usertype") != 'docente':
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def estudiante_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("usertype") != 'estudiante':
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function