from .processo_remover_negocio import ProcessoRemoverNegocio
from app import app
from ....utils.front_helper import *

@app.route('/processodois/remover/<processo_id>', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def processo_remover_2(processo_id):
    return ProcessoRemoverNegocio.exibir(processo_id)
