from .documento_editar_negocio import DocumentoEditarNegocio
from app import app
from ....utils.front_helper import *

@app.route('/documento7/<documento_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def documento_editar(documento_id):
    return DocumentoEditarNegocio.exibir(documento_id)
