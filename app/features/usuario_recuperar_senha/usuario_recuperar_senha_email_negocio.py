from .usuario_recuperar_senha_form import *
from ...cursor import db
from ...utils.return_errors import return_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from flask import url_for, request, flash, redirect, render_template
from flask_mail import Message
from app import app, mail
from config import ADMINS
from itsdangerous import URLSafeTimedSerializer
from flask_json import json_response

class UsuarioRecuperarSenhaEmailNegocio:

	def exibir():
		form = UsuarioRecuperarSenhaEmailForm();

		if form.validate_on_submit():
			if db.verifica_existe_email(form.recupera_email.data) is not True:
				flash('Email inválido', 'erro')
				return redirect(url_for('reset'))

			id = db.get_usuario_pelo_email(email = form.recupera_email.data)

			if db.get_usuario_status(id = id):
				s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

				token = s.dumps(form.recupera_email.data , salt = "1234")

				link = 'http://127.0.0.1:5000' + url_for('reset_with_token', token=token, external = True)

				msg = Message('Recuperação de Senha', sender = ADMINS[0], recipients = [form.recupera_email.data])

				msg.body = 'Clique no link a seguir para definir sua nova senha: {}'.format(link)

				with app.app_context():
					mail.send(msg)

				flash('Verifique sua caixa de entrada para recuperar sua senha.', 'success')

			else:
				flash('Seu email precisa ser confirmado.', 'error')
			return redirect(url_for('login'))
		return render_template('usuario_recuperar_senha.html', form = form)

	def recuperar(token):
		try:
			s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
			email = s.loads(token, salt="1234", max_age=3600)
		except:
			flash('O link é inválido ou expirou.', 'erro')
			return redirect(url_for('login'))

		form = UsuarioNovaSenha()

		if form.validate_on_submit():
			if db.verifica_existe_email(email = email) is not True:
				flash('Email inválido', 'erro')
				return redirect(url_for('login'))
			senhaHash = Criptografador.gerar_hash(form.nova_senha.data, '')

			id = db.get_usuario_pelo_email(email = email)

			db.set_usuario_senha(id = id, senha = senhaHash)

			flash('Sua senha foi atualizada!', 'success')

			return redirect(url_for('login'))
		return render_template('usuario_recuperar_senha_token.html', form = form, token = token)
