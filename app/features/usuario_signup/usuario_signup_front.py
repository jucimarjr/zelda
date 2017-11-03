from app import app
from .usuario_signup_negocio import UsuarioSignupNegocio

app.config['JSON_ADD_STATUS'] = False

@app.route('/cadastrar',methods=['POST'])
def cadastrar():
    return UsuarioSignupNegocio.exibir()

@app.route('/confirm/<token>')
def confirm_email(token):
	return UsuarioSignupNegocio.confirm(token = token);
