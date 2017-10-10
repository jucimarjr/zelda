from .usuario_editar_negocio import UsuarioEditarNegocio
from app import app

@app.route('/usuario/<user_id>', methods=['GET', 'POST'])
def usuario_editar(user_id):
    return UsuarioEditarNegocio.exibir(user_id)
   