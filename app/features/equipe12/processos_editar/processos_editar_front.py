from .processos_editar_negocio import ProcessoEditarNegocio
from app import app
from ....utils.front_helper import *

@app.route('/processos12/editar/<processo_id>',methods=['GET','POST'])
@login_required
@verifica_permissao
def processos_editar_12(processo_id):
    return ProcessoEditarNegocio.exibir(processo_id)
