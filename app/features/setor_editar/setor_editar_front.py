from setor_editar_negocio import SetorEditarNegocio
from app import app

@app.route('/setor/<setor_id>', methods=['GET', 'POST'])
def setor_editar(setor_id):
    return SetorEditarNegocio.exibir(setor_id)
