from .processo_listar_negocio import ProcessoListarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/processo13')
@login_required
def processo_listar_13():
    return ProcessoListarNegocio.exibir()
