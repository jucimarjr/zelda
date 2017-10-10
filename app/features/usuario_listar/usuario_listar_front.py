from .usuario_listar_negocio import UsuarioListarNegocio
from app import app

@app.route('/usuario')
def usuario_listar():
    return UsuarioListarNegocio.exibir()