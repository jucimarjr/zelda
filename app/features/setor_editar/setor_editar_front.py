from .setor_editar_negocio import SetorEditarNegocio
from app import app
from ...utils.login_required import *

@app.route('/setor/<setor_id>', methods=['GET', 'POST'])
@login_required
def setor_editar(setor_id):
    return SetorEditarNegocio.exibir(setor_id)
