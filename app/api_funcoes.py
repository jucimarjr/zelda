from flask import Flask, request
from app.db_interface import Zelda
from app.funcionario import Funcionario
from app.setor import Setor

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
        login="rcm.eng",
        situacao=0,
        setor_nome="Engenharia de Computacação",
        setor_situacao=0,
        senha="rcm.eng2013"),

    Funcionario(
        nome="Ricardo Moraes",
        login="rcm.eng17",
        situacao=0,
        setor_nome="Engenharia Mecânica",
        setor_situacao=0,
        senha="rcm.eng2017"),
]
# -----------------------------------------------------------


@app.route("/get/funcionarios", methods=['GET'])
def get_funcionarios():
    if request.method == 'GET':
        # funcionarios = db.get_funcionarios()
        return funcionarios.__str__()
    else:
        return ERROR_REQUEST_MESSAGE

@app.route("/get/usuarios/setor?=<setor_nome>", methods=['GET'])
def get_usuarios(self, setor = setor_nome):

    if request.method == 'GET':
       usuarios = db.get_usuarios(self.setor)
       return usuarios.__str__()

    else:
        return ERROR_REQUEST_MESSAGE
        


if __name__ == '__main__':
    app.run(host=IP,
            port=PORT,
            debug=DEBUG)
