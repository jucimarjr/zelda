from ...authentication import *
from ...utils.flash_errors import flash_errors
from .login_form import LoginForm
from flask import redirect, request, render_template, flash, url_for
from ..usuario_signup.usuario_signup_form import UsuarioSignupForm

class LoginNegocio:

    def exibir():
        form = LoginForm()
        sngform = UsuarioSignupForm()

        if form.validate_on_submit():

            login = form.login.data
            senha = form.senha.data

            if autentica(login, senha):
                return redirect(url_for('home'))

            flash("Nome de usuário ou senha incorretos.")
        else:
            print(request.method)
            if request.method != 'GET':
                flash_errors(form)

        return render_template('login.html', form = form, form_signup = sngform)
