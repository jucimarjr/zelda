from .funcionario_cadastrar_negocio import FuncionarioCadastrarNegocio
from app import app
from ...cursor import db

@app.route('/funcionario/novo', methods=['GET', 'POST'])
def funcionario_cadastrar():
    return FuncionarioCadastrarNegocio.exibir(db)