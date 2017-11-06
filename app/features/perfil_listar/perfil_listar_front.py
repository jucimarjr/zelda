from .perfil_listar_negocio import PerfilListarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/perfil', methods=['GET', 'POST'])
@login_required
@verifica_permissao
def perfil_listar():
    return PerfilListarNegocio.exibir()
