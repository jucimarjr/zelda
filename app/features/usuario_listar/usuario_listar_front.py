from usuario_listar_negocio import UsuarioListarNegocio

@app.route('/funcionario')
def funcionario_listar():
    return UsuarioListarNegocio.exibir()