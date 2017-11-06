from .setor_listar_negocio import SetorListarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/setor')
@login_required
@verifica_permissao
def setor_listar():
    return SetorListarNegocio.exibir()
