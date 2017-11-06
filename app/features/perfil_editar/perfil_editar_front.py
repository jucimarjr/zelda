from .perfil_editar_negocio import PerfilEditarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/perfil/<perfil_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def perfil_editar(perfil_id):
   return PerfilEditarNegocio.exibir(perfil_id)
 