from .funcionalidade_cadastrar_negocio import FuncionalidadeCadastrarNegocio
from app import app
from ...utils.login_required import *

@app.route('/funcionalidade/novo', methods=['GET', 'POST'])
@login_required
def funcionalidade_cadastrar():
    return FuncionalidadeCadastrarNegocio.exibir()
