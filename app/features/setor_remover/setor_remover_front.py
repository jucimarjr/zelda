from .setor_remover_negocio import SetorRemoverNegocio
from app import app
from ...utils.front_helper import *

@app.route('/setor/desativar/<setor_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def setor_desativar(setor_id):
    return SetorRemoverNegocio.exibir(setor_id)
