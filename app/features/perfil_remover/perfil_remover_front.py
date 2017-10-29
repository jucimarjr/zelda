from .perfil_remover_negocio import PerfilRemoverNegocio
from app import app
from ...utils.login_required import *

@app.route('/perfil/remover/<perfil_id>',methods=['GET','POST'])
@login_required
def perfil_remover(perfil_id):
    return PerfilRemoverNegocio.exibir(perfil_id)
