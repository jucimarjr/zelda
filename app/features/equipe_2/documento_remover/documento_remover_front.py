from .documento_remover_negocio import DocumentoRemoverNegocio
from app import app
from ....utils.front_helper import *

@app.route('/documentodois/remover/<documento_id>', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def documento_remover_2(documento_id):
    return DocumentoRemoverNegocio.exibir(documento_id)
