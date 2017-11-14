from app import app
from .....utils.front_helper import login_required, verifica_permissao
from .processo_remover_negocio import ProcessoRemoverNegocio

@app.route('/equipe1/processo/remover/<processo_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo_remover(processo_id):
    return ProcessoRemoverNegocio.exibir(processo_id)