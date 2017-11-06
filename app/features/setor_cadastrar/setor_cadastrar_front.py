from .setor_cadastrar_negocio import SetorCadastrarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/setor/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def setor_cadastrar():
    return SetorCadastrarNegocio.exibir()
