from funcionario_remover_negocio import FuncionarioRemoverNegocio
from app import app

@app.route('/funcionario/desativar', methods=['GET', 'POST'])
def funcionario_desativar():
    return FuncionarioRemoverNegocio.exibir()