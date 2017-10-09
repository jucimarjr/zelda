from .setor_remover_negocio import SetorRemoverNegocio
from app import app
from ...cursor import db

@app.route('/setor/desativar/<setor_id>', methods=['GET', 'POST'])
def setor_desativar(setor_id):
    return SetorRemoverNegocio.exibir(setor_id, db)
