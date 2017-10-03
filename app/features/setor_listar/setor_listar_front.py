from setor_listar_negocio import SetorListarNegocio

@app.route('/setor')
def setor_listar():
    return SetorListarNegocio.exibir()
