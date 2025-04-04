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
    "database": "db_abastecimento_semecti"
}

def executar_consulta(query, params=None, fetch=False):
    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(query, params or ())
    
    resultado = None
    if fetch:
        resultado = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()

    return resultado

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

    # Pegue os dados do usuário logado, por exemplo, o departamento
    departamento_usuario = session.get("departamento")  # Supondo que o departamento está armazenado na sessão
    
    return render_template("index.html", departamento_usuario=departamento_usuario)


@app.route("/login", methods=["POST"])
def do_login():
    nome_completo = request.form["nome_completo"]
    senha = request.form["senha"]

    query = "SELECT * FROM usuarios WHERE nome_completo = %s AND senha = %s"
    usuario = executar_consulta(query, (nome_completo, senha), fetch=True)

    if usuario:
        session["usuario"] = usuario[0]["nome_completo"]
        session["departamento"] = usuario[0]["departamento"]  # Armazena o cargo
        return redirect(url_for("index"))
    else:
        return render_template("login.html", error_message="Credenciais inválidas.")


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

    # Alteração para filtrar registros apenas de março (mês 3)
    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoAlmox 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

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

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoCasaDeProjetos 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)


                # COMUNICAÇÃO #

@app.route("/abastecimentoComunAut", methods=["POST"])
def registrar_abastecimentoComunicacao():
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
        INSERT INTO abastecimentoComunicacao (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoComunHist", methods=["GET"])
def listar_abastecimentosComunicacao():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoComunicacao 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)




                # DEE #

@app.route("/abastecimentoDEEAut", methods=["POST"])
def registrar_abastecimentoDEE():
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
        INSERT INTO abastecimentoDEE (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoDEEHist", methods=["GET"])
def listar_abastecimentosDEE():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoDEE 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)



                # engenharia manutenção#

@app.route("/abastecimentoEng1Aut", methods=["POST"])
def registrar_abastecimentoEng1():
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
        INSERT INTO abastecimentoEng1 (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoEng1Hist", methods=["GET"])
def listar_abastecimentosEng1():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoEng1 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)



# engenharia projetos #

@app.route("/abastecimentoEng2Aut", methods=["POST"])
def registrar_abastecimentoEng2():
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
        INSERT INTO abastecimentoEng2 (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoEng2Hist", methods=["GET"])
def listar_abastecimentosEng2():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoEng2 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)



# gabinete #

@app.route("/abastecimentoGabineteAut", methods=["POST"])
def registrar_abastecimentoGabinete():
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
        INSERT INTO abastecimentoGabinete (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoGabineteHist", methods=["GET"])
def listar_abastecimentosGabinete():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoGabinete 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)


# Informatica #

@app.route("/abastecimentoInformaticaAut", methods=["POST"])
def registrar_abastecimentoInformatica():
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
        INSERT INTO abastecimentoInformatica (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoInformaticaHist", methods=["GET"])
def listar_abastecimentosInformatica():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoInformatica 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)



# Logistica #

@app.route("/abastecimentoLogisticaAut", methods=["POST"])
def registrar_abastecimentoLogistica():
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
        INSERT INTO abastecimentoLogistica (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoLogisticaHist", methods=["GET"])
def listar_abastecimentosLogistica():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoLogistica 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)

# Núcleo #

@app.route("/abastecimentoNucleoAut", methods=["POST"])
def registrar_abastecimentoNucleo():
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
        INSERT INTO abastecimentoNucleo (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoNucleoHist", methods=["GET"])
def listar_abastecimentosNucleo():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoNucleo 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)


# Nutricao #

@app.route("/abastecimentoNutricaoAut", methods=["POST"])
def registrar_abastecimentoNutricao():
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
        INSERT INTO abastecimentoNutricao (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoNutricaoHist", methods=["GET"])
def listar_abastecimentosNutricao():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoNutricao 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)


# SUPERVISAO #

@app.route("/abastecimentoSupervisaoAut", methods=["POST"])
def registrar_abastecimentoSupervisao():
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
        INSERT INTO abastecimentoSupervisao (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoSupervisaoHist", methods=["GET"])
def listar_abastecimentosSupervisao():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoSupervisao 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)


# VIGILANCIA #

@app.route("/abastecimentoVigilanciaAut", methods=["POST"])
def registrar_abastecimentoVigilancia():
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
        INSERT INTO abastecimentoVigilancia (nome, rgf, km, placa, data, posto, comprovante)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, rgf, km, placa, data, posto, caminho_comprovante))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("index"))

@app.route("/abastecimentoVigilanciaHist", methods=["GET"])
def listar_abastecimentosVigilancia():
    if "usuario" not in session:
        return redirect(url_for("login"))

    query = """
        SELECT id, nome, rgf, km, placa, DATE_FORMAT(data, '%d/%m/%Y') AS data, posto, comprovante 
        FROM abastecimentoVigilancia 
        WHERE MONTH(data) = 4
    """
    abastecimentos = executar_consulta(query, fetch=True)

    return jsonify(abastecimentos)

if __name__ == "__main__":
    app.run(debug=True)
