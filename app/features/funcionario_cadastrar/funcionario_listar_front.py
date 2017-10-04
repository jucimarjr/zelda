from funcionario_listar_negocio import FuncionarioCadastrarNegocio
from app import app
from ...cursor import db

@app.route('/funcionario/novo', methods=['GET', 'POST'])
def funcionario_criar():
    return FuncionarioCadastrarNegocio.exibir(db)