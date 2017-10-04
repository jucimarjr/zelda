from .funcionario_listar_negocio import FuncionarioListarNegocio
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from app import app

@app.route('/funcionario')
def funcionario_listar():
    return FuncionarioListarNegocio.exibir()