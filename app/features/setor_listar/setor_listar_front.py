from .setor_listar_negocio import SetorListarNegocio
from app import app
from ...utils.login_required import *

@app.route('/setor')
@login_required
def setor_listar():
    return SetorListarNegocio.exibir()
