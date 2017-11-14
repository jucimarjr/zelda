from .processos_listar_negocio import ProcessoListarNegocio
from app import app
from ....utils.front_helper import *

@app.route('/processo13')
@login_required
@verifica_permissao
def processos_listar_13():
    return ProcessoListarNegocio.exibir()
