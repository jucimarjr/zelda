from .processo_listar_negocio import ProcessoListarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe8/processo')
@login_required
@verifica_permissao
def processo8_listar():
    return ProcessoListarNegocio.exibir()

