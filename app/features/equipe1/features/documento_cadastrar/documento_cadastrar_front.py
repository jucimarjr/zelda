from .documento_cadastrar_negocio import DocumentoCadastrarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe1/processo/<processo_id>/documento/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def equipe1_documento_cadastrar(processo_id):
    return DocumentoCadastrarNegocio.exibir(processo_id)
