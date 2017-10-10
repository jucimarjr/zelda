from .setor_listar_negocio import SetorListarNegocio
from app import app

@app.route('/setor')
def setor_listar():
    return SetorListarNegocio.exibir()
