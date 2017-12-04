from .documento_cadastrar_negocio import DocumentoCadastrarNegocio
from app import app
from .....utils.front_helper import *


@app.route('/equipe8/documento/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao

def documento8_cadastrar():
    return DocumentoCadastrarNegocio.exibir()