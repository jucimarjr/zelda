from .processo_remover_negocio import ProcessoRemoverNegocio
from app import app
from ...utils.front_helper import *

@app.route('/processo5/desativar/<processo_id>', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def processo_desativar_5(processo_id):
    return ProcessoRemoverNegocio.exibir(processo_id)
