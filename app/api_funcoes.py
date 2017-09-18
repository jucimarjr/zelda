from flask import Flask, request
#from db_interface import Zelda
from funcionario import Funcionario
from setor import Setor
from usuario import Usuario

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

@app.rout("/get/usuarios",methods = ['GET'])
def id():
    # funcionarios = db.get_usuarios()
    if request.method =='GET':
        return usuarios.___str___()
    else:
        return ERROR_REQUEST_MESSAGE
    
@app.route("/get/funcionarios", methods=['GET'])
def get_funcionarios():
    if request.method == 'GET':
        # funcionarios = db.get_funcionarios()
        return funcionarios.__str__()
    else:
        return ERROR_REQUEST_MESSAGE

@app.route("/get/funcionarios/setor?=<setor_nome>", methods=['GET'])
def get_funcionarios(self, setor = setor_nome):
    if request.method == 'GET':
       funcionarios = db.get_funcionarios(self.setor_nome)
       return funcionarios.__str__()
    else:
        return ERROR_REQUEST_MESSAGE

@app.route("/get/usuarios/setor/<nome_setor>", methods=['GET'])
def get_usuarios(nome_setor):
    if request.method == 'GET':
       usuarios = db.get_usuarios(nome_setor)
       return usuarios.__str__()
    else:
        return ERROR_REQUEST_MESSAGE


if __name__ == '__main__':
    app.run(host=IP,
            port=PORT,
            debug=DEBUG)
