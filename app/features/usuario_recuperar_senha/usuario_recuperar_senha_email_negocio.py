from .usuario_recuperar_senha_form import *
from ...cursor import db
from ...tables.usuario.usuario_modelo import Usuario
from flask import url_for, request, flash, redirect, render_template
from app import app, mail
from ...utils.mailer import enviar_email_recuperacao, extrair_token
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.flash_errors import *
from ...authentication import encerra_sessao

class UsuarioRecuperarSenhaEmailNegocio:

	def exibir():
		encerra_sessao()

		form = UsuarioRecuperarSenhaEmailForm()

		if form.validate_on_submit():
			data = db.verifica_existe_email(form.recupera_email.data)
			if len(data) < 1:
				flash('Email não cadastrado no sistema')
				return redirect(url_for('enviar_recuperacao_senha'))

			usuario = Usuario(data[0]['usuario_id'])

			enviar_email_recuperacao(usuario)
			return redirect(url_for('login'))
		else:
			flash_errors(form)

		return render_template('usuario_recuperar_senha.html', form = form)

	def recuperar(token):
		encerra_sessao()

		result = extrair_token(token)
		if result is None:
			flash('O link expirou ou é inválido')
			return redirect(url_for('login'))

		form = UsuarioNovaSenha()
		usuario = Usuario(result)

		if form.validate_on_submit():
			usuario.set_senha(form.nova_senha.data)

			flash('Sua senha foi atualizada!', 'success')
			return redirect(url_for('login'))
		else:
			flash_errors(form)

		return render_template('usuario_alterar_senha.html', form = form, token = token)
