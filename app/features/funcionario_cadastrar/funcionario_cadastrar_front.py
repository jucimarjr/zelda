from .funcionario_cadastrar_negocio import FuncionarioCadastrarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/funcionario/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def funcionario_cadastrar():
    return FuncionarioCadastrarNegocio.exibir()