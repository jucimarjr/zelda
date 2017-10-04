from usuario_editar_negocio import UsuarioEditarNegocio
from app import app
from ...cursor import db

@app.route('/usuario/<user_id>', methods=['GET', 'POST'])
def usuario_editar(user_id):
    return UsuarioEditarNegocio.exibir(user_id, db)
   