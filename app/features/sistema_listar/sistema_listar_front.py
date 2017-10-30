from .sistema_listar_negocio import SistemaListarNegocio
from app import app
from ...utils.login_required import *


@app.route('/sistema')
@login_required
def sistema_listar():
    return SistemaListarNegocio.exibir()