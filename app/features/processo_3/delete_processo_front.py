from .delete_processo_negocio import CrudProcessoDeletarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/processo_crud/delete/<delete_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo_crud_deletar(delete_id):
	return CrudProcessoDeletarNegocio.exibir(delete_id)