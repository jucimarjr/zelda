from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from forms import CadastraFuncionarioForms, LoginForms
from flask.ext.login import LoginManager, logout_user, login_user, current_user , login_required
#from classes import CriptografiaSenha

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jesus'
app.config['MYSQL_DB'] = 'zelda'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app) 

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#tela login
@app.route('/')
def index():
    form = LoginForms()
    return render_template("login.html",form=form)

'''@app.route("/login", methods=['POST'])
def login():
	form = Login_form()
	email = request.form['usuario']
	
	 # Create cursor
    cur = mysql.connection.cursor()
    
    result = cur.execute("SELECT funcionario_login FROM zelda_funcionario WHERE funcionario_login = 'jailsonpj' SELECT funcionario_login FROM zelda_funcionario WHERE funcionario_login = 'jailsonpj'")
	
	#dados_usuario = usuarios.query.filter_by(email=email).first()
	if dados_usuario != None:
		senha = request.form['senha']
		gerarSenha = CriptografiaSenha(senha)
		HashGerada = gerarSenha.gerarHash(dados_usuario.salt)
		
		if HashGerada == dados_usuario.senha:
			login_user(dados_usuario)
		

	
	
	return redirect(url_for('index'))
	


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/menu/Cadastrar Funcionario', methods=['GET', 'POST'])
def cadastrar_funcionario():
    form = FuncionarioCadastroForms(request.form)
    if request.method == 'POST' and form.validate():
        
        funcionario_id = form.funcionario_id.data
        funcionario_nome = form.funcionario_nome.data
        funcionario_login =form.funcionario_login.data
        funcionario_senha = sha256_crypt.encrypt(str(form.funcionario_senha.data))
        funcionario_email = form.funcionario_email.data
        funcionario_status = form.funcionario_status.data
        funcionario_matricula = form.funcionario_matricula.data
        funcionario_ultimo_acesso = form.funcionario_ultimo_acesso.data
        funcionario_enviados = form.funcionario_enviados.data
        funcionario_recebidos = form.funcionario_recebidos.data
        funcionario_telefone = form.funcionario_telefone.data
        funcionario_unidade = form.funcionario_unidade.data
        
        
        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO zelda_funcionario(funcionario_id, funcionario_nome, funcionario_login, funcionario_senha, funcionario_email, funcionario_status, funcionario_matricula, funcionario_ultimo_acesso, funcionario_enviados, funcionario_recebidos, funcionario_telefone, funcionario_unidade)  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (funcionario_id, funcionario_nome, funcionario_login, funcionario_senha, funcionario_email, funcionario_status, funcionario_matricula, funcionario_ultimo_acesso, funcionario_enviados, funcionario_recebidos, funcionario_telefone, funcionario_unidade))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Funcionario Cadastrado', 'success')

        return redirect(url_for('login'))
    return render_template('cadastrar_funcionario.html', form=form)
    

#@app.route('/menu/Remover Funcionario')
#def remover_funcionario():


#@app.route('/menu/Editar Funcionario')
#def editar_funcionario():
    
#@app.route('/menu/Cadastrar Setor',methods = ['GET', 'POST'])
#def cadastrar_setor():

#@app.route('/menu/Remover Setor')
#def remover_setor():

#@app.route('/menu/Editar Setor')
#def editar_setor():'''


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
