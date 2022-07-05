# Funciones para acceder a la BD

import sqlite3
from hashBcrypt import validarHash
import sys

# Verificar que usuario existe y enviar a que valide contraseña
def validarUsuario(username, contrasena):
    # Conectar a BD
    conexion = sqlite3.connect('basedatos.db')
    print("Base de datos abierta correctamente")

    # Objeto para ejecutar consultas en BD
    cur = conexion.cursor()

    # Consulta para extraer hash de la contraseña de BD
    cur.execute("SELECT hashContrasena FROM usuarios WHERE username=?", (username,))
    # Obtiene respuesta de la consulta
    respuesta = cur.fetchall()
    
    # Respuesta puede ser vacía, manejo de error
    try:
        # SQLite responde con una lista de tuplas
        # Seleccionamos primera tupla y primer elemento de la misma
        hashpass = respuesta[0][0]
    except:
        print("Ups!", sys.exc_info()[0], "ocurrio.")
        print("Retorno False")
        # Devolver False por error
        return False

    # Desconectar BD
    conexion.close()

    # Validar hash con la contraseña brindada
    return validarHash(contrasena, hashpass)

# Extraer tipo de Usuario
def validarTipoUsuario(username):
    # Conectar a BD
    conexion = sqlite3.connect('basedatos.db')
    print("Base de datos abierta correctamente")

    # Objeto para ejecutar consultas en BD
    cur = conexion.cursor()

    # Extraer contrasena de BD
    cur.execute("SELECT tipoUsuario FROM usuarios WHERE username=?", (username,))
    # Obtiene respuesta de la consulta
    respuesta = cur.fetchall()
    # Respuesta puede ser vacía, manejo de error    
    try:
        # SQLite responde con una lista de tuplas
        # Seleccionamos primera tupla y primer elemento de la misma
        tipoUsuario = respuesta[0][0]
    except:
        print("Ups!", sys.exc_info()[0], "ocurrio.")
        print("Retorno False")
        return False

    # Desconectar BD
    conexion.close()
    
    return tipoUsuario