from .processo_editar_negocio import ProcessoEditarNegocio
from app import app
from ....util.front_helper import *

@app.route('/processos/editar/<processo_id>',methods=['GET','POST'])
@login_required
@verifica_permissao
def processo_editar(processo_id):
    return ProcessoEditarNegocio.exibir(processo_id)
