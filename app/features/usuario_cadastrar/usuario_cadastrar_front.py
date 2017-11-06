from .usuario_cadastrar_negocio import UsuarioCadastrarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/usuario/novo', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def usuario_cadastrar():
   return UsuarioCadastrarNegocio.exibir()