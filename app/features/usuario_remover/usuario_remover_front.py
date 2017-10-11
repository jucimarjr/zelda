from .usuario_remover_negocio import UsuarioRemoverNegocio
from app import app
from ...utils.login_required import *

@app.route('/usuario/remover/<user_id>', methods=['GET', 'POST'])
@login_required
def usuario_remover(user_id):
    return UsuarioRemoverNegocio.exibir(user_id)
