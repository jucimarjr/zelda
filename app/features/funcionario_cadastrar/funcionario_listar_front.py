from funcionario_listar_negocio import FuncionarioCadastrarNegocio
from app import app

@app.route('/funcionario/novo', methods=['GET', 'POST'])
def funcionario_criar():
    return FuncionarioCadastrarNegocio.exibir()