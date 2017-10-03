from usuario_cadastrar_negocio import UsuarioCadastrarNegocio

@app.route('/usuario/novo', methods=['GET', 'POST'])
def usuario_criar():
   return UsuarioCadastrarNegocio.exibir()