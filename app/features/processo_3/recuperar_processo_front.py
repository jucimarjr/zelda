from .recuperar_processo_negocio import CrudProcessoRecuperaNegocio
from app import app
from ...utils.front_helper import *

@app.route('/processo_crud/recuperar', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def processo_crud_recuperar():
    return CrudProcessoRecuperaNegocio.exibir()