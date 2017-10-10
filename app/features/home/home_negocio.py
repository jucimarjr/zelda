from flask import render_template, redirect, url_for
from ...cursor import db
from ...authentication import verifica_sessao, retorna_usuario

class HomeNegocio():
    
    def exibir():
        if verifica_sessao() == True:
            return redirect(url_for('login'))
        
        usuario = retorna_usuario()
        return render_template('usuario_home.html', usuario=usuario)

class AdminNegocio():
    
    def exibir():
        if verifica_sessao() == True:
            return redirect(url_for('login'))
        
        usuario = retorna_usuario()
        return render_template('admin_home.html', usuario=usuario)