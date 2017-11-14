from .processos_listar_negocio import ProcessoListarNegocio
from app import app
from ....utils.front_helper import *

@app.route('/processos')
@login_required
@verifica_permissao
def processos_listar_12():
    return ProcessoListarNegocio.exibir()
