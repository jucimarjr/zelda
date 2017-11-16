from .documento_cadastrar_negocio import DocumentoCadastrarNegocio
from app import app
from ....utils.front_helper import *

@app.route('/documentodois/novo', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def documento_cadastrar_2():
    return DocumentoCadastrarNegocio.exibir()
