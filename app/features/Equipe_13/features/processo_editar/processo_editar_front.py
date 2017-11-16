from .processo_editar_negocio import ProcessoEditarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/processo_13/<processo_id>', methods=['GET', 'POST'])
@login_required
def processo_editar_13(processo_id):
    return ProcessoEditarNegocio.exibir(processo_id)
