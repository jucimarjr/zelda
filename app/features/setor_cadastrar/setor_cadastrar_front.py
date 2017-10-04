from setor_cadastrar_negocio import SetorCadastrarNegocio
from app import app

@app.route('/setor')
def setor_cadastrar():
    return SetorCadastrarNegocio.exibir()
