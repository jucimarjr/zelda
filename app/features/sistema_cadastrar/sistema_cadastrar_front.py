from .sistema_cadastrar_negocio import SistemaCadastrarNegocio
from app import app
from ...utils.login_required import *

@app.route('/sistema/novo', methods=['GET', 'POST'])
@login_required
def sistema_cadastrar():
    return SistemaCadastrarNegocio.exibir()
