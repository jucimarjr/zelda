from flask import render_template, flash, redirect, url_for, request
from .setor_editar_form import EditarSetorForm
from ...tables.setor.setor_modelo import Setor
from ...utils.flash_errors import flash_errors
from ...authentication import verifica_sessao
from ...cursor import db

class SetorEditarNegocio:    
    def exibir(setor_id):        
        form = EditarSetorForm()

        setor = Setor()

        if request.method == 'GET':

            setor = db.get_setor(setor_id)

            if setor is not None:
                form.setor_nome.data = setor.nome
                form.setor_id.data = setor.id
            else:
                return redirect(url_for('setor_listar'))

        elif form.validate_on_submit():
            setor.nome = form.setor_nome.data
            setor.id = form.setor_id.data

            db.edita_setor(setor)

            return redirect(url_for('setor_listar'))
        else:
            flash_errors(form)

        return render_template('setor_editar.html', form=form)