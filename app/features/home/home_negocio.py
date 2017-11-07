from flask import render_template, redirect, url_for
from ...cursor import db
from ...authentication import retorna_usuario
from ..usuario_confirmar_email.usuario_confirmar_email_form import ConfirmarEmailForm

class HomeNegocio():
    def exibir():
        form = ConfirmarEmailForm()
        usuario = retorna_usuario()
        form.usuario_id.data = usuario.get_id()
        form.email.data = usuario.email
        return render_template('home.html', form = form, usuario = usuario, funcionalidades = usuario.get_perfil().get_funcionalidades() )