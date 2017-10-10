from ...authentication import *
from ...utils.flash_errors import flash_errors
from .login_form import LoginForm
from flask import redirect, render_template, flash, url_for

class LoginNegocio:

    def exibir():
        form = LoginForm()

        if form.validate_on_submit():
            user_login = form.login.data
            user_senha = form.senha.data
            inicia_sessao(user_login = user_login)
            if (autentica(user_senha)):
                if (is_logado()):
                    db.set_logado_true(user_login)
                    if (is_admin()):
                        return redirect(url_for('admin_home'))
                    return redirect(url_for('index'))
                flash("Usuario já logado!")
                encerra_sessao()
            flash("Nome de usuário ou senha incorretos")
            encerra_sessao()
        else:
            flash_errors(form)

        return render_template('login.html', form=form)