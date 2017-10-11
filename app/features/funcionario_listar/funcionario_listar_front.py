from .funcionario_listar_negocio import FuncionarioListarNegocio
from app import app
from ...utils.login_required import *

@app.route('/funcionario')
@login_required
def funcionario_listar():
    return FuncionarioListarNegocio.exibir()