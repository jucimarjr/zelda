from .processo_cadastrar_negocio import ProcessoCadastrarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/processocinco/novo', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def processo_cadastrar_5():
    return ProcessoCadastrarNegocio.exibir()
