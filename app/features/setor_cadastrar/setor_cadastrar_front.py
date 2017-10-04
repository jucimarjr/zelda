from .setor_cadastrar_negocio import SetorCadastrarNegocio
from ...cursor import db
from app import app

@app.route('/setor/novo', methods=['GET', 'POST'])
def setor_cadastrar():
    return SetorCadastrarNegocio.exibir(db)
