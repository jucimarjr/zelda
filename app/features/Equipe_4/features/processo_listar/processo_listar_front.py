from .processo_listar_negocio import ProcessoListarNegocio
from app import app
from app.utils.front_helper import *

@app.route('/equipe4/processo')
#@login_required
def processo_listar_4():
    return ProcessoListarNegocio.exibir()
