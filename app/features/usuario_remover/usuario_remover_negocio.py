from flask import Flask, render_template, flash, redirect, url_for, request
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario

class UsuarioRemoverNegocio:
    
    def exibir(user_id):
        usuario = Usuario(user_id)
        if usuario.get_id() is None:
            return redirect(url_for('usuario_listar'))

        if request.method == 'POST':
            usuario.deleta()
            return redirect(url_for('usuario_listar'))
        
        return render_template('usuario_remover.html', usuario = usuario)