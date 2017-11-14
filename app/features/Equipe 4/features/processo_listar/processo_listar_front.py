from .processo_listar_negocio import ProcessoListarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/processo')
@login_required
def processo_listar():
    return ProcessoListarNegocio.exibir()
