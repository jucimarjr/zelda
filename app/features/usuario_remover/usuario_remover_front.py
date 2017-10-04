from usuario_remover_negocio import UsuarioRemoverNegocio
from app import app
from ...cursor import db

@app.route('/usuario/remover', methods=['GET', 'POST'])
def usuario_remover():
    return UsuarioRemoverNegocio.exibir(db)