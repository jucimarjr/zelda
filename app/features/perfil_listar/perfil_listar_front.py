from .perfil_listar_negocio import PerfilListarNegocio
from app import app
from ...utils.login_required import *

@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil_listar():
    return PerfilListarNegocio.exibir()
