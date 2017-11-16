from .documento_cadastrar_negocio import DocumentoCadastrarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe4/processo/<processo_id>/documento/novo', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def documento_cadastrar_4(processo_id):
    return DocumentoCadastrarNegocio.exibir(processo_id)
