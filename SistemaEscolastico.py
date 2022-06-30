from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Servidor Web para el Sistema Escolastico con Flask</h1><h2>Grupo # 3 - Ing Software 1</h2>"