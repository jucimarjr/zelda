from .documento_editar_negocio import DocumentoEditarNegocio
from app import app
from .....utils.front_helper import *


@app.route('/processo8/<processo_id>/editar/<documento_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao

def documento_editar():
    return DocumentoEditarNegocio.exibir(processo_id)