from app import app
from .....utils.front_helper import login_required, verifica_permissao
from .processo_editar_negocio import ProcessoEditarNegocio

@app.route('/equipe1/processo/<processo_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo_editar(processo_id):
    return ProcessoEditarNegocio.exibir(processo_id)