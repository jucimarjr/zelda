from .documento_cadastrar_negocio import DocumentoCadastrarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe_11/documento/novo', methods=['GET', 'POST'])
@login_required
#@verifica_permissao
def documento_cadastrar():
    usuarios = ZeldaModelo.lista_usuarios()
    return DocumentoCadastrarNegocio.exibir()
