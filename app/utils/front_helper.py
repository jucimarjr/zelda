from functools import wraps
from flask import url_for, request, redirect, render_template, session, flash
from ..authentication import sessao_ativa, make_session_permanent, sessao_expirada, retorna_usuario
from .zelda_modelo import ZeldaModelo

def verifica_permissao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        funcionalidade_caminho = '/' + request.path.split('/')[1]
        
        funcionalidade = ZeldaModelo.pesquisa_funcionalidade(funcionalidade_caminho)
        usuario = retorna_usuario()

        if funcionalidade is not None:
            if usuario.pode_acessar(funcionalidade):
                return f(*args, **kwargs)

            flash('Você não tem acesso à funcionalidade "' + funcionalidade.nome + '"')
        else:
            flash('A funcionalidade de caminho "' + funcionalidade_caminho + '" não está cadastrada no sistema')

        return redirect(url_for('home'))
    return decorated_function

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if sessao_expirada():
            flash("Sessão expirada")

        if not sessao_ativa():
            return redirect(url_for('login'))

        make_session_permanent()

        return f(*args, **kwargs)
    return decorated_function