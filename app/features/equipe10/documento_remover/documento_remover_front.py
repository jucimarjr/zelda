from .documento_remover_negocio import DocumentoRemoverNegocio
from app import app
from ....utils.front_helper import *

@app.route('/equipe10/documento/remover/<documento_id>', methods=['GET', 'POST'])
#@login_required
#@verifica_permissao
def documento_desativar(documento_id):
    return DocumentoRemoverNegocio.exibir(documento_id)