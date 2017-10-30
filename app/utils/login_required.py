from functools import wraps
from flask import url_for, request, redirect, render_template
from ..authentication import sessao_ativa

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not sessao_ativa():
            return redirect(url_for('login'))

        return f(*args, **kwargs)
    return decorated_function