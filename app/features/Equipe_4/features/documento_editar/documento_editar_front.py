from .documento_editar_negocio import DocumentoEditarNegocio
from app import app
from .....utils.front_helper import *

@app.route('/equipe4/processo/<processo_id>/documento/<documento_id>', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def documento_editar_4(documento_id, processo_id):
    return DocumentoEditarNegocio.exibir(documento_id = documento_id, processo_id = processo_id)
