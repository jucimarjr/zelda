from usuario_remover_negocio import UsuarioRemoverNegocio

@app.route('/usuario/remover', methods=['GET', 'POST'])
def usuario_remover():
    return UsuarioRemoverNegocio.exibir()