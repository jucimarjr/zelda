from .sistema_remover_negocio import SistemaRemoverNegocio
from app import app
from ...utils.front_helper import *

@app.route('/sistema/desativar/<sistema_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def sistema_desativar(sistema_id):
    return SistemaRemoverNegocio.exibir(sistema_id)
