from .perfil_criar_negocio import PerfilCadastrarNegocio
from app import app
from ...utils.login_required import *

@app.route('/perfil/<perfil_id>', methods=['GET', 'POST'])
@login_required
def perfil_cadastrar():
   return PerfilEditarNegocio.exibir(<perfil_id>)
