from .crud_processo_negocio import CrudProcessoNegocio
from app import app
from ...utils.front_helper import *

@app.route('/processo_crud/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo_crud():
    return CrudProcessoNegocio.exibir()