from .editar_processo_negocio import CrudProcessoEditarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/processo_crud/editar/<editar_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo_crud_editar(editar_id):
	return CrudProcessoEditarNegocio.exibir(editar_id)