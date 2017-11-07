from app import app
from .usuario_signup_negocio import UsuarioSignupNegocio

app.config['JSON_ADD_STATUS'] = False

@app.route('/cadastrar',methods=['POST'])
def cadastrar():
    return UsuarioSignupNegocio.exibir()
