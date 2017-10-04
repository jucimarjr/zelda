from funcionario_remover_negocio import FuncionarioRemoverNegocio
from app import app
from ...cursor import db

@app.route('/funcionario/desativar', methods=['GET', 'POST'])
def funcionario_desativar():
    return FuncionarioRemoverNegocio.exibir(db)