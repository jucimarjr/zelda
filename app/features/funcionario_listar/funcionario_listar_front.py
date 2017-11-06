from .funcionario_listar_negocio import FuncionarioListarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/funcionario')
@login_required
@verifica_permissao
def funcionario_listar():
    return FuncionarioListarNegocio.exibir()