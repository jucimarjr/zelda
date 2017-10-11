from functools import wraps
from flask import url_for, request, redirect, render_template
from ..authentication import verifica_sessao

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if verifica_sessao() is True:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function