from setor_remover_negocio import SetorRemoverNegocio

@app.route('/setor/desativar', methods=['GET', 'POST'])
def setor_desativar():
    return SetorRemoverNegocio.exibir()
