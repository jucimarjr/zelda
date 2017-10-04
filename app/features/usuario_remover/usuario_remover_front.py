from usuario_remover_negocio import UsuarioRemoverNegocio
from app import app

@app.route('/usuario/remover', methods=['GET', 'POST'])
def usuario_remover():
    return UsuarioRemoverNegocio.exibir()