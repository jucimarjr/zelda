from .processo_listar_negocio import ProcessoListarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe_11/processo')
@login_required
#@verifica_permissao
def processo_listar():
    return ProcessoListarNegocio.exibir()