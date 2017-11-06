from .sistema_listar_negocio import SistemaListarNegocio
from app import app
from ...utils.front_helper import *


@app.route('/sistema')
@login_required
@verifica_permissao
def sistema_listar():
    return SistemaListarNegocio.exibir()