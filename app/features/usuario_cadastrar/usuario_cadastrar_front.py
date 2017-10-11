from .usuario_cadastrar_negocio import UsuarioCadastrarNegocio
from app import app
from ...utils.login_required import *

@app.route('/usuario/novo', methods=['GET', 'POST'])
@login_required
def usuario_cadastrar():
   return UsuarioCadastrarNegocio.exibir()