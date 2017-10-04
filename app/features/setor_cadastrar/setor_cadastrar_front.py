from .setor_cadastrar_negocio import SetorCadastrarNegocio
from app import app
from ...cursor import db

@app.route('/setor/novo')
def setor_cadastrar():
    return SetorCadastrarNegocio.exibir(db)
