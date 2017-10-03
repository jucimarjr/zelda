from usuario_editar_negocio import UsuarioEditarNegocio

@app.route('/usuario/<user_id>', methods=['GET', 'POST'])
def usuario_editar(user_id):
    return UsuarioEditarNegocio.exibir()
   