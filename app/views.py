from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from .classes import Criptografador
from flask_mysqldb import MySQL
from .db_interface import Zelda
from .features.login.login_form import LoginForm
from .features.criptografador.criptografador_negocio import Criptografador
from .features.funcionario_listar.funcionario_listar_front import funcionario_listar
from .features.funcionario_listar.funcionario_listar_negocio import FuncionarioListarNegocio
from .features.setor_listar.setor_listar_front import setor_listar
from .features.setor_listar.setor_listar_negocio import SetorListarNegocio
from .features.usuario_listar.usuario_listar_front import usuario_listar
from .features.usuario_listar.usuario_listar_negocio import UsuarioListarNegocio
from .authentication import *

from app import app

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'modelagemdeprogramas'
app.config['MYSQL_DB'] = 'zelda'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# init MYSQL
db = Zelda(app)


# Index
@app.route('/')
@app.route('/index')
def index():
    if(verifica_sessao):
        return redirect(url_for('login'))

    usuario = retorna_usuario
    return render_template('usuario_home.html', usuario=usuario)



# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user_login = form.login.data
        user_senha = form.senha.data
        inicia_sessao(user_login = user_login)
        if (autentica(user_senha, db)):
            if (is_logado(db)):
                set_logado(True, db)
                if (is_admin(db)):
                    return redirect(url_for('admin_home'))
                return redirect(url_for('index'))
            flash("Usuario já logado!")
            encerra_sessao()
        flash("Nome de usuário ou senha incorretos")
        encerra_sessao()
    else:
        flash_errors(form)

    return render_template('login.html', form=form)


@app.route('/logout/')
def logout():
    encerra_sessao()
    return redirect(url_for('index'))


@app.route('/admin')
def admin_home():
    if(verifica_sessao):
        return redirect(url_for('login'))

    usuario = retorna_usuario()
    return render_template('admin_home.html', usuario = usuario)

'''
@app.route('/funcionario')
def funcionario_listar():
    if(session['user_login'] == ""):
        return redirect(url_for('index'))

    funcionarios = db.get_funcionarios()
    return render_template(
        'funcionario_listar.html',
        funcionarios=funcionarios)


@app.route('/usuario')
def usuario_listar():
    if(session['user_login'] == ""):
        return redirect(url_for('index'))

    usuarios = db.get_usuarios()
    return render_template('usuario_listar.html', usuarios=usuarios)


@app.route('/setor')
def setor_listar():
    if(session['user_login'] == ""):
        return redirect(url_for('index'))

    setores = db.get_setores()
    return render_template('setor_listar.html', setores=setores)


@app.route('/usuario/novo', methods=['GET', 'POST'])
def usuario_criar():
    if(session['user_login'] == ""):
        return redirect(url_for('index'))

    form = CadastraUsuarioForm()
    if form.validate_on_submit():
        usuario = Usuario(login=form.usuario_login.data, senha=Criptografador.gerar_hash(form.usuario_senha.data, ''), admin=form.usuario_admin.data - 1)

        db.cadastra_usuario(usuario)
        return redirect(url_for('usuario_listar'))
    else:
        flash_errors(form)
        return render_template('usuario_criar.html', form=form)


@app.route('/usuario/<user_id>', methods=['GET', 'POST'])
def usuario_editar(user_id):
    if(session['user_login'] == ""):
        return redirect(url_for('index'))

    form = AtualizaUsuarioForm()

    usuario = Usuario()

    if form.validate_on_submit():
        usuario.login = form.usuario_login.data
        usuario.id = form.usuario_id.data
        usuario.senha = Criptografador.gerar_hash(form.usuario_senha.data, '')
        usuario.admin = form.usuario_admin.data - 1

        db.edita_usuario(usuario)

        return redirect(url_for('usuario_listar'))
    else:

        usuario = db.get_usuario(user_id)

        if usuario is not None:
            form.usuario_admin.default = int(usuario.admin + 1)
            form.process()

            form.usuario_login.data = usuario.login
            form.usuario_id.data = user_id

        else:
            return redirect(url_for('usuario_listar'))

        flash_errors(form)

    return render_template('usuario_editar.html', form=form)


@app.route('/funcionario/novo', methods=['GET', 'POST'])
def funcionario_criar():
    if(session['user_login'] == ""):
        return redirect(url_for('index'))

    form = CadastraFuncionarioForm()

    # Recupera todos os setores do banco
    setores = db.get_setores_ativos()

    # Adiciona dinamicamente as opções do SelectField que vai ser renderizado
    # pelo wtforms
    form.funcionario_setor_id.choices = [(s.id, s.nome) for s in setores]
    form.funcionario_setor_id.default = 1  # O setor de id 1 no banco é o Nenhum

    if form.validate_on_submit():
        funcionario = Funcionario(nome=form.funcionario_nome.data)

        db.cadastra_funcionario(funcionario)
        funcionarios = db.get_funcionarios()

        lotacao = Lotacao(funcionario_id=len(funcionarios), setor_id=form.funcionario_setor_id.data)

        db.cadastra_lotacao(lotacao)
        return redirect(url_for('funcionario_listar'))
    else:
        flash_errors(form)
        return render_template('funcionario_criar.html', form=form, setores=setores)


@app.route('/funcionario/<func_id>', methods=['GET', 'POST'])
def funcionario_editar(func_id):
    if(session['user_login'] == ""):
        return redirect(url_for('index'))

    form = AtualizaFuncionarioForm()

    func = Funcionario()
    lotacao = Lotacao()

    # Recupera todos os setores do banco
    setores = db.get_setores()

    # Adiciona dinamicamente as opções do SelectField que vai ser renderizado
    # pelo wtforms
    form.setor_id.choices = [(s.id, s.nome) for s in setores]

    # Se a página foi carregada com dados post (do formulário da própria
    # página), valida os campos
    if form.validate_on_submit():

        # Preenche um novo funcionário com os campos atualizados
        func.nome = form.funcionario_nome.data
        func.id = form.funcionario_id.data

        db.edita_funcionario(func)

        lotacao = db.get_lotacao_ativa(func.id)

        # Verifica se o setor selecionado permanece inalterado
        if lotacao is None or lotacao.setor_id != form.setor_id.data:

            lotacao = Lotacao()

            # Se não, cadastra uma nova lotação
            lotacao.setor_id = form.setor_id.data
            lotacao.funcionario_id = func.id

            db.cadastra_lotacao(lotacao)

        return redirect(url_for('funcionario_listar'))

    # A página pode ser acessada diretamente pela URL ao passar somente o id
    # do item a ser editado
    else:
        # Recupera o funcionário no banco
        func = db.get_funcionario(func_id)

        # Se o id encontrou algum funcionário no banco
        if func is not None:

            # Recupera a lotação ativa do funcionário no banco
            lotacao = db.get_lotacao_ativa(func_id)
            preenche_dados_atuais(form, func, lotacao)

        else:
            # Se o id é inválido, redireciona para o menu
            return redirect(url_for('funcionario_listar'))

        flash_errors(form)

    return render_template('funcionario_editar.html', form=form)


def preenche_dados_atuais(form, func, lotacao):
    # Preenche o formulário com os dados atuais do funcionário

    if lotacao is not None:
        form.setor_id.default = int(lotacao.setor_id)
        form.lotacao_id.data = lotacao.id

    form.process()

    form.funcionario_nome.data = func.nome
    form.funcionario_id.data = func.id


@app.route('/funcionario/desativar', methods=['GET', 'POST'])
def funcionario_desativar():

    # Se a página foi acessada por post pelo form do WTForms da própria página
    if request.method == 'POST':

        ids = request.form.getlist("ids[]")
        if request.form['origem'] == 'propria':
            # Percorre a lista de ids do FieldList
            for item in ids:
                # do qual pegamos o primeiro e único elemento
                db.deleta_funcionario(item)
        # Se o form é inválido e a página foi acessada por POST
        else:
            funcionarios = []
            if ids is not None and len(ids) > 0:
                # Lista os dados de cada funcionário na lista de ids[]
                for func_id in ids:
                    funcionario = db.get_funcionario(func_id)
                    if funcionario is not None:
                        funcionarios.append(funcionario)
                return render_template('funcionario_desativar.html', form=request.form, funcionarios=funcionarios)
    """Se o método foi GET ou o form deu erro de submissão, redireciona pra
   página de listagem"""
    return redirect(url_for('funcionario_listar'))


@app.route('/setor/novo', methods=['GET', 'POST'])
def setor_criar():
    form = CadastraSetorForm()

    if form.validate_on_submit():
        setor = Setor(nome=form.setor_nome.data)

        db.cadastra_setor(setor)

        return redirect(url_for('setor_listar'))
    else:
        flash_errors(form)

    return render_template('setor_criar.html', form=form)


@app.route('/setor/<setor_id>', methods=['GET', 'POST'])
def setor_editar(setor_id):
    form = AtualizaSetorForm()

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


@app.route('/setor/desativar', methods=['GET', 'POST'])
def setor_desativar():
    # Se a página foi acessada por post pelo form do WTForms da própria página
    if request.method == 'POST':

        ids = request.form.getlist("ids[]")

        if request.form['origem'] == 'propria':

            for item in ids:
                # do qual pegamos o primeiro e único elemento
                db.deleta_setor(item)

        # Se o form é inválido e a página foi acessada por POST
        else:
            setores = []

            if ids is not None and len(ids) > 0:

                # Lista os dados de cada setor na lista de ids[]
                for set_id in ids:
                    setor = db.get_setor(set_id)

                    if setor is not None:
                        setores.append(setor)

                return render_template('setor_desativar.html', form=request.form, setores=setores)

    """Se o método foi GET ou o form deu erro de submissão, redireciona pra
    página de listagem"""
    return redirect(url_for('setor_listar'))


@app.route('/usuario/remover', methods=['GET', 'POST'])
def usuario_remover():
    form = RemoveUsuarioForm()
    if request.method == 'POST':

        ids = request.form.getlist("ids[]")

        if request.form['origem'] == 'propria':

            # Percorre a lista de ids do FieldList
            for item in ids:
                # do qual pegamos o primeiro e único elemento
                db.deleta_usuario(item)

        # Se o form é inválido e a página foi acessada por POST
        else:
            usuarios = []

            if ids is not None and len(ids) > 0:

                # Lista os dados de cada funcionário na lista de ids[]
                for user_id in ids:
                    usuario = db.get_usuario(user_id)

                    if usuario is not None:
                        usuarios.append(usuario)

                return render_template('usuario_remover.html', form=request.form, usuarios=usuarios)

    """Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem"""
    return redirect(url_for('usuario_listar'))

'''
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error))
