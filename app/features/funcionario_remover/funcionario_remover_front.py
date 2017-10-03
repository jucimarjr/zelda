from funcionario_remover_negocio import FuncionarioRemoverNegocio

@app.route('/funcionario/desativar', methods=['GET', 'POST'])
def funcionario_desativar():
    return FuncionarioRemoverNegocio.exibir()