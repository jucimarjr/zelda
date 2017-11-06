from .usuario_editar_negocio import UsuarioEditarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/usuario/<user_id>', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def usuario_editar(user_id):
    return UsuarioEditarNegocio.exibir(user_id)
   