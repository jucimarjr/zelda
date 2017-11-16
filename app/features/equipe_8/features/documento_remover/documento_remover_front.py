from .documento_remover_negocio import DocumentoRemoverNegocio
from app import app
from .....utils.front_helper import *


@app.route('/processo8/remover/<documento_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao

def documento_cadastrar():
    return DocumentoCadastrarNegocio.exibir(documento_id)