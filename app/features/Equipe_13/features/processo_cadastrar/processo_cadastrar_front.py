from app import app
from .....utils.front_helper import login_required, verifica_permissao
from .processo_cadastrar_negocio import ProcessoCadastrarNegocio

@app.route('/equipe1/processo/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def equipe1_processo_cadastrar():
    return ProcessoCadastrarNegocio.exibir()