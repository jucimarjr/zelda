from .funcionario_remover_negocio import FuncionarioRemoverNegocio
from app import app
from ...utils.front_helper import *

@app.route('/funcionario/desativar/<func_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def funcionario_desativar(func_id):
    return FuncionarioRemoverNegocio.exibir(func_id)