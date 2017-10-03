from setor_cadastrar_negocio import SetorCadastrarNegocio

@app.route('/setor')
def setor_cadastrar():
    return SetorCadastrarNegocio.exibir()
