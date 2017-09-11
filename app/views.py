from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home',)

@app.route('/cadastrar_funcionario')
def cadastroFuncionario():
    return render_template("CadastroFuncionario.html",title='Cadastrar Funcionario')

@app.route('/editar_funcionario')
def editarFuncionario():
    return render_template("EditarFuncionario.html",title='Editar Funcionario')
