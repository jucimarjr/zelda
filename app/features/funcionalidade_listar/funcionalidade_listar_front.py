from .funcionalidade_listar_negocio import FuncionalidadeListarNegocio
from app import app
from ...utils.login_required import *

@app.route('/funcionalidade')
@login_required
def funcionalidade_listar():
    return FuncionalidadeListarNegocio.exibir()
