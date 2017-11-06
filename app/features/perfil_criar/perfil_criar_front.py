from .perfil_criar_negocio import PerfilCadastrarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/perfil/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def perfil_cadastrar():
   return PerfilCadastrarNegocio.exibir()
