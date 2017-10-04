from .usuario_listar_negocio import UsuarioListarNegocio
from app import app
from ...cursor import db

@app.route('/funcionario')
def usuario_listar():
    return UsuarioListarNegocio.exibir(db)