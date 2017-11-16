from .documento_remover_negocio import DocumentoRemoverNegocio
from app import app
from ....utils.front_helper import *

@app.route('/documento7/remover/<documento_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def documento_remover(documento_id):
    return DocumentoRemoverNegocio.exibir(documento_id)
