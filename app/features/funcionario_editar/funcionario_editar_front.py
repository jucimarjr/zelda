from funcionario_editar_negocio import FuncionarioEditarNegocio
from app import app
from ...cursor import db

@app.route('/funcionario/<func_id>', methods=['GET', 'POST'])
def funcionario_editar(func_id):
   return FuncionarioEditarNegocio.exibir(func_id, db)