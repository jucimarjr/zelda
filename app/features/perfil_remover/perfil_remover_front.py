from .perfil_remover_negocio import PerfilRemoverNegocio
from app import app
from ...utils.front_helper import *

@app.route('/perfil/remover/<perfil_id>',methods=['GET','POST'])
@login_required
@verifica_permissao
def perfil_remover(perfil_id):
    return PerfilRemoverNegocio.exibir(perfil_id)
