from .funcionario_editar_negocio import FuncionarioEditarNegocio
from app import app
from ...utils.login_required import *

@app.route('/funcionario/<func_id>', methods=['GET', 'POST'])
@login_required
def funcionario_editar(func_id):
   return FuncionarioEditarNegocio.exibir(func_id)
