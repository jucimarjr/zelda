from flask import Flask, render_template, flash, redirect, url_for, request
from ...utils.flash_errors import flash_errors
from ...authentication import verifica_sessao
from ...cursor import db

class UsuarioRemoverNegocio:
    
    def exibir(user_id):
        if verifica_sessao() == True:
            return redirect(url_for('login'))

        usuario = db.get_usuario(user_id)
        if usuario is None:
            return redirect(url_for('usuario_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            db.deleta_usuario(user_id)
        else:
            return render_template('usuario_remover.html', usuario=usuario)
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra
    página de listagem"""
        return redirect(url_for('usuario_listar'))
