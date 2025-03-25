import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "chave_secreta"  # Para gerenciar sessões

# Configuração do banco de dados
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "raulgui123!",
    "database": "abastecimento_db"
}

# Função para conectar ao banco
def conectar_bd():
    return mysql.connector.connect(**db_config)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/comprovantes")
def comprovantes():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("comprovantes.html")

@app.route("/login", methods=["POST"])
def do_login():
    nome_completo = request.form["nome_completo"]
    senha = request.form["senha"]  # Senha em texto puro

    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    # Busca usuário pelo nome e senha (sem hash)
    cursor.execute("SELECT * FROM usuarios WHERE nome_completo = %s AND senha = %s", (nome_completo, senha))
    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    if usuario:
        session["usuario"] = usuario["nome_completo"]
        return redirect(url_for("index"))
    else:
        # Passando uma mensagem de erro para o template
        error_message = "Credenciais inválidas."
        return render_template("login.html", error_message=error_message)  # Passando a mensagem de erro

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
