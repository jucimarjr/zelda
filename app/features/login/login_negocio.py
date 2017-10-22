from ...authentication import *
from ...utils.flash_errors import flash_errors
from .login_form import LoginForm
from flask import redirect, render_template, flash, url_for
from ..usuario_signup.usuario_signup_form import UsuarioSignupForm

class LoginNegocio:

    def exibir():
        form = LoginForm()
        sngform = UsuarioSignupForm()

        if form.validate_on_submit():
            user_login = form.login.data
            user_senha = form.senha.data
            inicia_sessao(user_login = user_login)
            if (autentica(user_senha)):
                if (is_logado()):
                    db.set_logado_true(user_login)
                    return redirect(url_for('home'))
                flash("Usuario já logado!")
                encerra_sessao()
            flash("Nome de usuário ou senha incorretos")
            encerra_sessao()
        else:
            flash_errors(form)

        return render_template('login.html', form = form, form_signup = sngform)
        
