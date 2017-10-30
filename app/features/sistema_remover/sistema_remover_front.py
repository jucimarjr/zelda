from .sistema_remover_negocio import SistemaRemoverNegocio
from app import app
from ...utils.login_required import *

@app.route('/sistema/desativar/<sistema_id>', methods=['GET', 'POST'])
@login_required
def sistema_desativar(sistema_id):
    return SistemaRemoverNegocio.exibir(sistema_id)
