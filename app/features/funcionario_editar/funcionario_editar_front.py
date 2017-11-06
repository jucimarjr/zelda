from .funcionario_editar_negocio import FuncionarioEditarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/funcionario/<func_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def funcionario_editar(func_id):
   return FuncionarioEditarNegocio.exibir(func_id)
