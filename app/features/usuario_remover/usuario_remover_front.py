from .usuario_remover_negocio import UsuarioRemoverNegocio
from app import app

@app.route('/usuario/remover/<user_id>', methods=['GET', 'POST'])
def usuario_remover(user_id):
    return UsuarioRemoverNegocio.exibir(user_id)
