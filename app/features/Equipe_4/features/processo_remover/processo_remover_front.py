from .processo_remover_negocio import ProcessoRemoverNegocio
from app import app
from app.utils.front_helper import *

@app.route('/equipe4/processo/remover/<processo_id>', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def processo_remover_4(processo_id):
    return ProcessoRemoverNegocio.exibir(processo_id)
