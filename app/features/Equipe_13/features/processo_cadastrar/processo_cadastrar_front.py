from app import app
from .....utils.front_helper import login_required, verifica_permissao
from .processo_cadastrar_negocio import ProcessoCadastrarNegocio

@app.route('/equipe13/processo/novo', methods=['GET', 'POST'])
@login_required
def processo_cadastrar_13():
    return ProcessoCadastrarNegocio.exibir()
