from .processo_listar_negocio import ProcessoListarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/processocinco')
#@login_required
#@verifica_permissao
def processo_listar_5():
    return ProcessoListarNegocio.exibir()
