from .documento_listar_negocio import DocumentoListarNegocio
from app import app
from .....utils.front_helper import *


@app.route('/equipe8/documento', methods=['GET', 'POST'])
@login_required
@verifica_permissao

def documento8_listar():
    return DocumentoListarNegocio.exibir()