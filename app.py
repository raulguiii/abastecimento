import os
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "chave_secreta"  # Para gerenciar sessões

# Configuração do banco de dados
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "raulgui123!",
    "database": "db_abastecimento"
}

# Diretório para salvar os comprovantes
UPLOAD_FOLDER = "static/comprovantes/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Cria a pasta se não existir

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



                        # A L M O X A R I F A D O #

@app.route("/abastecimentoAlmoxarifadoAut", methods=["POST"])
def registrar_abastecimentoAlmox():
    if "usuario" not in session:
        return redirect(url_for("login"))

    nome = request.form["nome"]
    rgf = request.form["rgf"]
    km = request.form["km"]
    placa = request.form["placa"]
    data = request.form["data"]
    posto = request.form["posto"]

    if "comprovante" not in request.files:
        return "Erro: Nenhum arquivo enviado."
    
    file = request.files["comprovante"]
    if file.filename == "":
        return "Erro: Nome de arquivo inválido."

    caminho_comprovante = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(caminho_comprovante)

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO abastecimentoAlmox (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoAlmoxarifadoHist", methods=["GET"])
def listar_abastecimentosAlmox():
    if "usuario" not in session:
        return redirect(url_for("login"))

    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante FROM abastecimentoAlmox")
    abastecimentos = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(abastecimentos)




                    # CASA DE PROJETOS #

@app.route("/abastecimentoCasaDeProjetosAut", methods=["POST"])
def registrar_abastecimentoCasaDeProjetos():
    if "usuario" not in session:
        return redirect(url_for("login"))

    nome = request.form["nome"]
    rgf = request.form["rgf"]
    km = request.form["km"]
    placa = request.form["placa"]
    data = request.form["data"]
    posto = request.form["posto"]

    if "comprovante" not in request.files:
        return "Erro: Nenhum arquivo enviado."
    
    file = request.files["comprovante"]
    if file.filename == "":
        return "Erro: Nome de arquivo inválido."

    caminho_comprovante = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(caminho_comprovante)

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO abastecimentoCasaDeProjetos (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoCasaDeProjetosHist", methods=["GET"])
def listar_abastecimentosCasaDeProjetos():
    if "usuario" not in session:
        return redirect(url_for("login"))

    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante FROM abastecimentoCasaDeProjetos")
    abastecimentos = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(abastecimentos)




if __name__ == "__main__":
    app.run(debug=True)
