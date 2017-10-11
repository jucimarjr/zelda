from .funcionario_remover_negocio import FuncionarioRemoverNegocio
from app import app
from ...utils.login_required import *

@app.route('/funcionario/desativar/<func_id>', methods=['GET', 'POST'])
@login_required
def funcionario_desativar(func_id):
    return FuncionarioRemoverNegocio.exibir(func_id)