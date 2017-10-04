from .setor_remover_negocio import SetorRemoverNegocio
from app import app
from ...cursor import db

@app.route('/setor/desativar', methods=['GET', 'POST'])
def setor_desativar():
    return SetorRemoverNegocio.exibir(db)
