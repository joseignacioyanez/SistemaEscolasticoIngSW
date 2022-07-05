import sqlite3
# funcion para hacer hash de mismo directorio
from hashBcrypt import hashearContrasena

# Conectar a BD
conexion = sqlite3.connect('basedatos.db')
print("Base de datos abierta correctamente")

# Crear la BD en base a schema.sql
with open('schema.sql') as f:
    a = conexion.executescript(f.read())
    print(a)
    print("BD creada")

# Objeto para ejecutar consultas en BD
cur = conexion.cursor()

#Contrasenas Hashear
contrasenaAdmin = 'admin123'
hashContrasenaAdmin = hashearContrasena(contrasenaAdmin)
contrasenaJirafales = 'donaflorinda123'
hashContrasenaJirafales = hashearContrasena(contrasenaJirafales)
contrasenaPepito = 'pepita123'
hashContrasenaPepito = hashearContrasena(contrasenaPepito)

# Inserts
cur.execute("INSERT INTO usuarios (username, hashContrasena, tipoUsuario) VALUES (?, ?, ?)",
        ('admin', hashContrasenaAdmin, 'administrador'));

cur.execute("INSERT INTO usuarios (username, hashContrasena, tipoUsuario) VALUES (?, ?, ?)",
        ('profeJirafales', hashContrasenaJirafales, 'docente'));

cur.execute("INSERT INTO usuarios (username, hashContrasena, tipoUsuario) VALUES (?, ?, ?)",
        ('pepito', hashContrasenaPepito, 'estudiante'));

print("Insertado")

# Guardar Transacciones antes de Cerrar Conexion
conexion.commit()
# Cerrar Conexion
conexion.close()