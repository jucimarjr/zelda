from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from .forms import *
from .classes import Criptografador
from flask_mysqldb import MySQL
from .db_interface import Zelda
from .funcionario import Funcionario
from .setor import Setor

from app import app


# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'zelda'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
db = Zelda(app)



# Index
@app.route('/')
@app.route('/index')
def index():
    form = LoginForm()
    return render_template("login.html",form=form)

# User login
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['user_login'] = form.login.data
        senha = form.senha.data
        senhaHash = Criptografador.gerarHash(senha, '')

        # Backdoor do administrador
        if form.login.data == "jailson_admin" and senhaHash == "110d46fcd978c24f306cd7fa23464d73":
            return redirect(url_for('admin'))

        ans = db.verifica_login(login = form.login.data, senha = senhaHash)
        if ans:
            if (not db.verifica_logado(login = form.login.data)):
                db.set_logado_true(login = form.login.data)
                if (db.verifica_admin(login = form.login.data)):
                    return redirect(url_for('admin'))
                return redirect(url_for('home'))
            flash("Usuario já logado!")

        else:
            flash("Nome de usuário ou senha incorretos")
    else:
        flash_errors(form)

    return render_template('login.html', form=form)

@app.route('/logout/')
def logout():
    session.pop('username', None)
    user_login = session.get('user_login', None)
    db.set_logado_false(user_login)
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    form = CadastraFuncionarioForm()
    return render_template('TelaAdmin.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/funcionario')
def funcionario_listar():
    funcionarios = db.get_funcionarios();
    return render_template('funcionario_listar.html', funcionarios= funcionarios);

@app.route('/usuario')
def usuario_listar():
    funcionarios = db.get_funcionarios();
    return render_template('Usuario_listar.html', funcionarios= funcionarios);


@app.route('/funcionario/novo', methods=['GET','POST'])
def funcionario_criar():
    form = CadastraFuncionarioForm()

    # Recupera todos os setores do banco
    setores = db.get_setores_ativos()

    # Adiciona dinamicamente as opções do SelectField que vai ser renderizado pelo wtforms
    form.funcionario_setor_id.choices = [(s.id, s.nome) for s in setores]
    form.funcionario_setor_id.default = 1 # O setor de id 1 no banco é o Nenhum

    if form.validate_on_submit():
        funcionario = Funcionario(nome = form.funcionario_nome.data, login = form.funcionario_login.data,senha =
        Criptografador.gerarHash(form.funcionario_senha.data, ''), setor_id = form.funcionario_setor_id.data)

        db.cadastra_funcionario(funcionario)
        return redirect(url_for('funcionario_listar'))
    else:
        flash_errors(form)
        return render_template('funcionario_criar.html',form=form, setores=setores)


@app.route('/funcionario/<func_id>', methods=['GET','POST'])
def funcionario_atualizar(func_id):
    form = AtualizaFuncionarioForm()

    func = Funcionario()

    # Recupera todos os setores do banco
    setores = db.get_setores()

    # Adiciona dinamicamente as opções do SelectField que vai ser renderizado pelo wtforms
    form.funcionario_setor_id.choices = [(s.id, s.nome) for s in setores]

    # Se a página foi carregada com dados post (do formulário da própria página), valida os campos
    if form.validate_on_submit():

        # Preenche um novo funcionário com os campos atualizados
        func.nome = form.funcionario_nome.data
        func.id = form.funcionario_id.data
        func.login = form.funcionario_login.data
        func.senha = form.funcionario_senha.data
        func.setor_id = form.funcionario_setor_id.data

        db.edita_funcionario(func)

        return redirect(url_for('funcionario_listar'))

    # A página pode ser acessada diretamente pela URL ao passar somente o id do item a ser editado
    else:

        # Verifica se o id foi passado na URL
        func_id = request.args["id"]

        # Recupera o funcionário no banco
        func = db.get_funcionario(func_id)

        # Se o id encontrou algum funcionário no banco
        if func is not None:
            preenche_dados_atuais(form, func)

        else:
            # Se o id é inválido, redireciona para o menu
            return redirect(url_for('funcionario_listar'))

        flash_errors(form)

    return render_template('funcionario_atualizar.html', form=form)


def preenche_dados_atuais(form, func):
    # Preenche o formulário com os dados atuais do funcionário
    form.funcionario_setor_id.default = int(func.setor_id)
    form.process()

    form.funcionario_nome.data = func.nome
    form.funcionario_id.data = func.id
    form.funcionario_login.data = func.login
    form.funcionario_senha.data = func.senha


@app.route('/funcionario/desativar', methods=['GET','POST'])
def funcionario_remover():
    form = RemoveFuncionarioForm()

    # Se a página foi acessada por post pelo form do WTForms da própria página
    if form.validate_on_submit():

        # Percorre a lista de ids do FieldList
        for list_item in form.data.funcionarios_ids:

            # Formato do FieldList fica assim:
            '''
            {
                funcionarios_ids-0: [id_0],
                funcionarios_ids-1: [id_1],
                ...
            }
            '''
            # então o list_item pego no for é puramente o array
            '''
            [id_i]
            '''
            # do qual pegamos o primeiro e único elemento

            db.deleta_funcionario(list_item[0])

    # Se o form é inválido e a página foi acessada por POST
    elif request.method != 'GET':

        funcionarios = []
        ids_funcionarios = request.form.getlist('ids[]')

        # Se há um parâmetro post chamado ids[], então a página foi acessa da página de listagem
        if ids_funcionarios is not None and len(ids_funcionarios) > 0:

            # Lista os dados de cada funcionário na lista de ids[]
            for func_id in ids_funcionarios:
                funcionario = db.get_funcionario(func_id)

                if funcionario is not None:
                    funcionarios.append(funcionario)

            return render_template('remover_funcionario.html', form=form, funcionarios=funcionarios)

    # Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem
    return redirect(url_for('funcionario_listar'))


@app.route('/setor/novo', methods=['GET','POST'])
def setor_criar():
    form = CadastraSetorForm()

    if form.validate_on_submit():
        setor = Setor(nome=form.setor_nome.data)

        db.cadastra_setor(setor)

        return redirect(url_for('admin'))
    else:
        flash_errors(form)

    return render_template('setor_criar.html', form=form)

@app.route('/setor/<setor_id>', methods=['GET','POST'])
def setor_atualizar(setor_id):
    form = AtualizaSetorForm()

    setor = Setor()

    if request.method == 'GET':
        setor_id = request.args["id"]

        setor = db.get_setor(setor_id)

        if setor is not None:
            form.setor_nome.data = setor.nome
            form.setor_id.data = setor.id
        else:
            return redirect(url_for('admin'))

    elif form.validate_on_submit():
        setor.nome = form.setor_nome.data
        setor.id = form.setor_id.data

        db.edita_setor(setor)

        return redirect(url_for('admin'))
    else:
        flash_errors(form)

    return render_template('setor_atualizar.html', form=form)


@app.route('/setor/desativar', methods=['GET', 'POST'])
def remover_setor():
    form = RemoveSetorForm()

    setor = Setor()

    if form.validate_on_submit():
        db.deleta_setor(form.setor_id.data)
        return redirect(url_for('admin'))
    else:

        setor_id = request.args['id']

        setor = db.get_setor(setor_id)

        if setor is None:
            return redirect(url_for('admin'))
        else:
            form.setor_id.data = setor.id

        flash_errors(form)

    return render_template('remover_setor.html', form=form, setor=setor)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
