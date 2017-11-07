from ...utils.flash_errors import flash_errors
from .usuario_confirmar_email_form import ConfirmarEmailForm
from ...cursor import db
from ...utils.mailer import Mailer, extrair_token, enviar_email_confirmacao
from ...tables.usuario.usuario_modelo import Usuario
from ...authentication import encerra_sessao, inicia_sessao
from flask import flash, redirect, url_for

class ConfirmarEmailNegocio():
    def enviar():
        form = ConfirmarEmailForm()

        if form.validate_on_submit():
            usuario = Usuario(form.usuario_id.data)

            data = db.verifica_existe_email(form.email.data)
            if len(data) > 0:
                if str(data[0]['usuario_id']) != str(usuario.get_id()):
                    flash('O email já está cadastrado')
                    return redirect(url_for('home'))

            usuario.email = form.email.data
            usuario.salva()

            enviar_email_confirmacao(usuario)
        else:
            flash_errors(form)

        return redirect(url_for('home'))

    def confirmar(token):
        result = extrair_token(token)

        if result is not None:
            usuario = Usuario(result)

            if result != usuario.get_id():
                encerra_sessao()
                inicia_sessao(usuario.get_id())

            usuario.ativa()
            flash('Sua conta foi ativada')
        else:
            flash('O link expirou ou é inválido')

        return redirect(url_for('home'))
