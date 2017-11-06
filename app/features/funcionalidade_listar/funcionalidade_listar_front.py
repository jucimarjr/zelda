from .funcionalidade_listar_negocio import FuncionalidadeListarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/funcionalidade')
@login_required
@verifica_permissao
def funcionalidade_listar():
    return FuncionalidadeListarNegocio.exibir()
