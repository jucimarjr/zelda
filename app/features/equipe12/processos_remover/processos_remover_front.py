from .processos_remover_negocio import ProcessoRemoverNegocio
from app import app
from ....utils.front_helper import *

@app.route('/processos12/remover/<processo_id>',methods=['GET','POST'])
@login_required
@verifica_permissao
def processos_remover_12(processo_id):
    return ProcessoRemoverNegocio.exibir(processo_id)
