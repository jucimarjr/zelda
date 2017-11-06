from .sistema_cadastrar_negocio import SistemaCadastrarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/sistema/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def sistema_cadastrar():
    return SistemaCadastrarNegocio.exibir()
