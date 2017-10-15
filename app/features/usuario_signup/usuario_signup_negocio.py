from flask_json import json_response
from .usuario_signup_form import UsuarioSignupForm
from ...cursor import db
from ...utils.return_errors import return_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador

class UsuarioSignupNegocio:

    def exibir():
        form = UsuarioSignupForm()

        if form.validate_on_submit():
            if db.verifica_email(form.signup_email.data) is not True:
                usuario = Usuario(login = form.signup_login.data,
                    senha = Criptografador.gerar_hash(form.signup_senha.data,''),
                    email = form.signup_email.data)
                db.cadastra_usuario(usuario)
                return json_response(mensagem="Cadastrado")
            else:
                return json_response(mensagem="Email ja cadastrado no sistema")
        else:
            return json_response(mensagem=return_errors(form))
            
