import bcrypt

def hashearContrasena(contrasena):
    # Codificar como Sal
    contrasenaBytes = contrasena.encode('utf-8')
    # Generar Sal
    miSal = bcrypt.gensalt()
    hasheado = bcrypt.hashpw(contrasenaBytes, miSal)
    print("hasheado")
    return hasheado 

def validarHash(contrasena, hash):
    contrBytes = contrasena.encode('utf-8')
    return bcrypt.checkpw(contrBytes, hash)

