from .processo_cadastrar_negocio import ProcessoCadastrarNegocio
from app import app
from app.utils.front_helper import *

@app.route('/equipe4/processo/novo', methods=['GET', 'POST'])
#@login_required
def processo_cadastrar():
   return ProcessoCadastrarNegocio.exibir()
