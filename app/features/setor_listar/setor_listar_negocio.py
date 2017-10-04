from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from ...setor.setor_interface import SetorInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL
from ...authentication import verifica_sessao

class SetorListarNegocio:
    def exibir(db):
        if(verifica_sessao() == True):
            return redirect(url_for('login'))

        setores = db.get_setores()
        return render_template('setor_listar.html', setores=setores)