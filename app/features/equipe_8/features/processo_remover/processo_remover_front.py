from .processo_remover_negocio import ProcessoRemoverNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe8/processo/remover/<processo_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo8_remover(processo_id):
    return ProcessoRemoverNegocio.exibir(processo_id)
