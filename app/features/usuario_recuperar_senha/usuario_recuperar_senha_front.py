from app import app
from .usuario_recuperar_senha_email_negocio import UsuarioRecuperarSenhaEmailNegocio

@app.route('/reset', methods=["GET", "POST"])
def enviar_recuperacao_senha():
	return UsuarioRecuperarSenhaEmailNegocio.exibir()

@app.route('/reset/<token>', methods=["GET", "POST"])
def recuperar_senha(token):
	return UsuarioRecuperarSenhaEmailNegocio.recuperar(token = token)
