from .documento_listar_negocio import DocumentoListarNegocio
from app import app
from .....utils.front_helper import *


@app.route('/processo8', methods=['GET', 'POST'])
@login_required
@verifica_permissao

def documento_listar():
    return DocumentoListarNegocio.exibir()