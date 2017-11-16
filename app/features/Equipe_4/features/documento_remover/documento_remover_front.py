from app import app
from .....utils.front_helper import *
from .documento_remover_negocio import DocumentoRemoverNegocio

@app.route('/equipe4/processo/<processo_id>/documento/remover/<documento_id>', methods = ['GET', 'POST'])
#@login_required
#@verifica_permissao
def documento_remover_4(processo_id, documento_id):
    return DocumentoRemoverNegocio.exibir(processo_id, documento_id)
