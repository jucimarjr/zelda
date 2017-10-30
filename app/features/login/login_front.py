from .login_negocio import LoginNegocio
from app import app
from flask import redirect, url_for
from ...authentication import sessao_ativa


@app.route('/login', methods=['GET','POST'])
def login():
    if sessao_ativa():
        return redirect(url_for('home'))
    
    return LoginNegocio.exibir()
