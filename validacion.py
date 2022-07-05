import sqlite3
from hashBcrypt import validarHash
import sys

def validarUsuario(username, contrasena):
    # Conectar a BD
    conexion = sqlite3.connect('basedatos.db')
    print("Base de datos abierta correctamente")

    # Objeto para ejecutar consultas en BD
    cur = conexion.cursor()

    # Extraer contrasena de BD
    cur.execute("SELECT hashContrasena FROM usuarios WHERE username=?", (username,))
    respuesta = cur.fetchall()
    try:
        hashpass = respuesta[0][0]
    except:
        print("Ups!", sys.exc_info()[0], "ocurrio.")
        return False

    conexion.close()

    return validarHash(contrasena, hashpass)

def validarTipoUsuario(username):
    # Conectar a BD
    conexion = sqlite3.connect('basedatos.db')
    print("Base de datos abierta correctamente")

    # Objeto para ejecutar consultas en BD
    cur = conexion.cursor()

    # Extraer contrasena de BD
    cur.execute("SELECT tipoUsuario FROM usuarios WHERE username=?", (username,))
    respuesta = cur.fetchall()
    try:
        tipoUsuario = respuesta[0][0]
    except:
        print("Ups!", sys.exc_info()[0], "ocurrio.")
        print("Retorno False")
        return False

    conexion.close()

    return tipoUsuario