#from flask_json import json_response
from .usuario_signup_form import UsuarioSignupForm
from ...cursor import db
from ...utils.return_errors import return_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from flask import url_for, request, flash, redirect
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from flask_json import json_response
from ...utils.mailer import Mailer, enviar_email_confirmacao
from ...authentication import inicia_sessao

class UsuarioSignupNegocio:

	def exibir():
		form = UsuarioSignupForm()

		if form.validate_on_submit():
			if len(db.verifica_existe_email(form.signup_email.data)) > 0:
				return json_response(mensagem=["Email já cadastrado no sistema"], tipo = "warning")

			if len(db.verifica_existe_login(form.signup_login.data)) > 0:
				return json_response(mensagem=["Login já cadastrado no sistema"], tipo = "warning")

			usuario = Usuario()
			usuario.login = form.signup_login.data
			usuario.email = form.signup_email.data
			usuario.salva()

			usuario.set_senha(form.signup_senha.data)

			enviar_email_confirmacao(usuario)

			inicia_sessao(usuario.get_id())

			return json_response(mensagem = "Você foi cadastrado com sucesso", tipo = "success")
		else:
			return json_response(mensagem=return_errors(form), tipo = "danger")
