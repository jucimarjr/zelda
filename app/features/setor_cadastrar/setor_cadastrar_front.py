from .setor_cadastrar_negocio import SetorCadastrarNegocio
from app import app
from ...utils.login_required import *

@app.route('/setor/novo', methods=['GET', 'POST'])
@login_required
def setor_cadastrar():
    return SetorCadastrarNegocio.exibir()
