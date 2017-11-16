from .documento_cadastrar_negocio import DocumentoCadastrarNegocio
from app import app
from .....utils.front_helper import *


@app.route('/processo8/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao

def documento_cadastrar():
    return DocumentoCadastrarNegocio.exibir(documento_id)