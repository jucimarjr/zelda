from setor_remover_negocio import SetorRemoverNegocio
from app import app

@app.route('/setor/desativar', methods=['GET', 'POST'])
def setor_desativar():
    return SetorRemoverNegocio.exibir()
