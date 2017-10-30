from .login_negocio import LoginNegocio
from app import app
from flask import redirect, url_for, session
from ...authentication import sessao_ativa
from datetime import timedelta

@app.route('/login', methods=['GET','POST'])
def login():
    if sessao_ativa():
        return redirect(url_for('home'))
    
    return LoginNegocio.exibir()

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)
