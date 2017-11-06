from .funcionalidade_editar_negocio import FuncionalidadeEditarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/funcionalidade/editar/<funcionalidade_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def funcionalidade_editar(funcionalidade_id):
    return FuncionalidadeEditarNegocio.exibir(funcionalidade_id)
