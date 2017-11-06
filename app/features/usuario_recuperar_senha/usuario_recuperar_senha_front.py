from app import app
from .usuario_recuperar_senha_email_negocio import UsuarioRecuperarSenhaEmailNegocio

@app.route('/reset', methods=["GET", "POST"])
def reset():
	return UsuarioRecuperarSenhaEmailNegocio.exibir()

@app.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
	return UsuarioRecuperarSenhaEmailNegocio.recuperar(token = token)
