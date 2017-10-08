from .funcionario_remover_negocio import FuncionarioRemoverNegocio
from app import app
from ...cursor import db

@app.route('/funcionario/desativar/<func_id>', methods=['GET', 'POST'])
def funcionario_desativar(func_id):
    return FuncionarioRemoverNegocio.exibir(func_id, db)