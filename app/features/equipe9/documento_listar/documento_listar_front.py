from .documento_listar_negocio import DocumentoListarNegocio
from app import app
from ....utils.front_helper import *

@app.route('/documento9')
@login_required
@verifica_permissao
def documento_listar():
    return DocumentoListarNegocio.exibir()
