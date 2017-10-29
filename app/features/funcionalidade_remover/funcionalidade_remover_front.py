from .funcionalidade_remover_negocio import FuncionalidadeRemoverNegocio
from app import app
from ...utils.login_required import *

@app.route('/funcionalidade/desativar/<funcionalidade_id>', methods=['GET', 'POST'])
@login_required
def funcionalidade_desativar(funcionalidade_id):
    return FuncionalidadeRemoverNegocio.exibir(funcionalidade_id)
