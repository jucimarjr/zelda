from funcionario_listar_negocio import FuncionarioListarNegocio
from flash_errors_negocio import FlashErrorsNegocio


@app.route('/funcionario')
def funcionario_listar():
    return FuncionarioListarNegocio.exibir()