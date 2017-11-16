from .processo_cadastrar_negocio import processoCadastrarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe_11/processo/novo', methods=['GET', 'POST'])
@login_required
#@verifica_permissao
def processo_cadastrar():
    usuarios = ZeldaModelo.lista_usuarios()
    return processoCadastrarNegocio.exibir()
