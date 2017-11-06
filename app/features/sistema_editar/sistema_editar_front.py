from .sistema_editar_negocio import SistemaEditarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/sistema/<sistema_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def sistema_editar(sistema_id):
    return SistemaEditarNegocio.exibir(sistema_id)
