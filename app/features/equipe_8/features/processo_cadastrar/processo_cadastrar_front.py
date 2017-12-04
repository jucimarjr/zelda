from .processo_cadastrar_negocio import ProcessoCadastrarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe8/processo/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo8_cadastrar():
    return ProcessoCadastrarNegocio.exibir()
