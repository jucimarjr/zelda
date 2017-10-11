from .funcionario_cadastrar_negocio import FuncionarioCadastrarNegocio
from app import app
from ...utils.login_required import *

@app.route('/funcionario/novo', methods=['GET', 'POST'])
@login_required
def funcionario_cadastrar():
    return FuncionarioCadastrarNegocio.exibir()