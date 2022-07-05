DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hashContrasena BLOB NOT NULL, /* Para guardar hashes en bytes https://stackabuse.com/hashing-passwords-in-python-with-bcrypt/ */
    tipoUsuario TEXT NOT NULL
);