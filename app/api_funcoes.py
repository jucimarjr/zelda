from flask import Flask, request
from db_interface import Zelda
from funcionario import Funcionario
from setor import Setor

ERROR_REQUEST_MESSAGE = "Error: only GET methods are available"

# Configuração do servidor da API
IP = '127.0.0.1'
PORT = 3600
DEBUG = False
app = Flask(__name__)
# -------------------------------

# Configuração do Banco de Dados acessado pela API
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'jesus'
# app.config['MYSQL_DB'] = 'mzelda'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# ------------------------------------------------

# Criando instância da Class de Interface do Banco de Dados
# db = Zelda(app)
# ---------------------------------------------------------

# Criação de funcionários para não ser necessário requisitar informações do BD
funcionarios = [
    Funcionario(
        nome="Rodrigo Moraes",
        situacao=0,
        setor_nome="Engenharia de Computacação",
        setor_situacao=0),

    Funcionario(
        nome="Ricardo Moraes",
        situacao=0,
        setor_nome="Engenharia Mecânica",
        setor_situacao=0),
]
# ------------------------------------------------------------------------------

# Criação de usuários para não ser necessário requisitar informações do BD
usuarios = [
	Usuario(
		login="rcm.eng",
        senha="rcm.eng"),

	Usuario(
		login="rcm.eng17",
        senha="rcm.eng17")
]
# ------------------------------------------------------------------------

@app.route("/get/funcionarios", methods=['GET'])
def get_funcionarios():
    if request.method == 'GET':
        # funcionarios = db.get_funcionarios()
        return funcionarios.__str__()
    else:
        return ERROR_REQUEST_MESSAGE

if __name__ == '__main__':
    app.run(host=IP,
            port=PORT,
            debug=DEBUG)
