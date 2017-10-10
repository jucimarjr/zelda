from .funcionario_listar_negocio import FuncionarioListarNegocio
from app import app

@app.route('/funcionario')
def funcionario_listar():
    return FuncionarioListarNegocio.exibir()