#from flask_json import json_response
from .usuario_signup_form import UsuarioSignupForm
from ...cursor import db
from ...utils.return_errors import return_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from flask import url_for, request, flash
from flask_mail import Message
from app import app, mail
from config import ADMINS
from itsdangerous import URLSafeTimedSerializer
from flask_json import json_response




s = URLSafeTimedSerializer("testesecreto")

class UsuarioSignupNegocio:

    def exibir():
        form = UsuarioSignupForm()

        if form.validate_on_submit():
            if db.verifica_existe_email(form.signup_email.data) is not False:
                return json_response(mensagem="Email ja cadastrado no sistema")

            if db.verifica_existe_login(form.signup_login.data) is not False:
                return json_response(mensagem="Login já cadastrado no sistema")

            usuario = Usuario()
            usuario.login = form.signup_login.data
            usuario.senha = Criptografador.gerar_hash(form.signup_senha.data,'')
            usuario.email = form.signup_email.data
            usuario.salva()


            token = s.dumps(usuario.email, salt = "1234")

            msg = Message('Email de confirmação', sender = ADMINS[0], recipients = [usuario.email])

            link = 'http://127.0.0.1:5000' + url_for('home', token=token, external = True)


            msg.body = 'Bem vindo! Clique no link a seguir para confirmar seu endereço de email: {}'.format(link)

            with app.app_context():
                mail.send(msg)

            return json_response(mensagem="Um email foi enviado para o endereço \"{}\". Confirme sua conta.".format(usuario.email))
        else:
            return json_response(mensagem=return_errors(form))
