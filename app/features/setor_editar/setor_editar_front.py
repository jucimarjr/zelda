from .setor_editar_negocio import SetorEditarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/setor/<setor_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def setor_editar(setor_id):
    return SetorEditarNegocio.exibir(setor_id)
