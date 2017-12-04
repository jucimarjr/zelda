from .processo_editar_negocio import ProcessoEditarNegocio
from app import app
from ....utils.front_helper import *

@app.route('/processo9/<processo_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo9_editar(processo_id):
    return ProcessoEditarNegocio.exibir(processo_id)
