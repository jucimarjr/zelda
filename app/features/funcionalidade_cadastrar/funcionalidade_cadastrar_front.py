from .funcionalidade_cadastrar_negocio import FuncionalidadeCadastrarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/funcionalidade/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def funcionalidade_cadastrar():
    return FuncionalidadeCadastrarNegocio.exibir()
