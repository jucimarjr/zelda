from .usuario_cadastrar_negocio import UsuarioCadastrarNegocio
from app import app
from ...cursor import db

@app.route('/usuario/novo', methods=['GET', 'POST'])
def usuario_cadastrar():
   return UsuarioCadastrarNegocio.exibir(db)