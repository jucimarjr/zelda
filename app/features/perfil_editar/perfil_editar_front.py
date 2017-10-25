from .perfil_editar_negocio import PerfilEditarNegocio
from app import app
from ...utils.login_required import *

@app.route('/perfil/<perfil_id>', methods=['GET', 'POST'])
@login_required
def perfil_editar():
   return PerfilEditarNegocio.exibir(perfil_id)
 