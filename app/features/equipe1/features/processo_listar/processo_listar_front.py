from app import app
from .....utils.front_helper import login_required, verifica_permissao
from .processo_listar_negocio import ProcessoListarNegocio

@app.route('/equipe1')
@app.route('/equipe1/processo')
@login_required
@verifica_permissao
def equipe1_processo_listar():
    return ProcessoListarNegocio.exibir()