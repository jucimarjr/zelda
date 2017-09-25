from flask_mysqldb import MySQL
from .funcionario import Funcionario
from .setor import Setor
#from .usuario import Usuario

class Zelda:

    def __init__(self, app):
        self.mysql = MySQL(app)

    def execute_query(self, query, insert=False):
        cur = self.mysql.connection.cursor()
        cur.execute(query)
        if insert:
          self.mysql.connection.commit()
        else:
          data = cur.fetchall()
          cur.close()
          return data

    def verifica_login(self, login, senha):
        data = self.execute_query("select count(*) from funcionario where funcionario_login = '{}' and funcionario_senha = '{}'".format(login, senha))
        return int(data[0]['count(*)']) > 0

    #função que verifica se o usuário está logado. Utilizado no login único.
    def verifica_logado(self, login):
        data = self.execute_query("select funcionario_logado from funcionario where funcionario_login = '{}'".format(login))
        if (data[0]['funcionario_logado'] == 1):
            return False
        return True

    def set_logado_true(self, login):
        data = self.execute_query("select funcionario_id from funcionario where funcionario_login = '{}'".format(login))
        self.execute_query("update funcionario set funcionario_logado = 0 where funcionario_id = '{}'".format(data[0]['funcionario_id']), True)

    def set_logado_false(self, login):
        data = self.execute_query("select funcionario_id from funcionario where funcionario_login = '{}'".format(login))
        self.execute_query("update funcionario set funcionario_logado = 1 where funcionario_id = '{}'".format(data[0]['funcionario_id']), True)

    def verifica_admin(self, login):
        data = self.execute_query("select funcionario_admin from funcionario where funcionario_login = '{}'".format(login))
        if (data[0]['funcionario_admin'] == 1):
            return False
        return True

    def set_admin_true(self, login):
        data = self.execute_query("select funcionario_id from funcionario where funcionario_login = '{}'".format(login))
        self.execute_query("update funcionario set funcionario_admin = 0 where funcionario_id = '{}'".format(data[0]['funcionario_id']), True)

    def get_funcionario_senha(self, login):
        data = self.execute_query("select funcionario_senha from funcionario where funcionario_login = '{}'".format(login))
        return data

	# CRUD - USUARIO
    def cadastra_usuario(self, usuario):
        self.execute_query("insert into usuario (usuario_login, usuario_senha, usuario_logado, usuario_admin) values ('{}', '{}', '{}', '{}')".format(usuario.login, usuario.senha, usuario.logado, usuario.admin), True)

    def get_usuarios(self):
        data = self.execute_query("select * from usuario")
        usuarios = []
        for u in data:
            usuario = Usuario(
				id=u["usuario_id"],
				login=u["usuario_login"],
				senha=u["usuario_senha"],
				logado=u["usuario_logado"],
				admin=u["usuario_admin"])
            usuarios.append(usuario)
        return usuarios

    def get_usuarios_logados(self):
        data = self.execute_query("select * from usuario where usuario_logado = 1")
        usuarios = []
        for u in data:
        	usuario = Usuario(
        		id=u["usuario_id"],
        		login=u["usuario_login"],
        		senha=u["usuario_senha"],
        		logado=u["usuario_logado"],
        		admin=u["usuario_admin"])
        	usuarios.append(usuario)
        return usuarios

    def get_usuarios_admin(self):
        data = self.execute_query("select * from usuario where usuario_admin = 1")
        usuarios = []
        for u in data:
        	usuario = Usuario(
        		id=u["usuario_id"],
        		login=u["usuario_login"],
        		senha=u["usuario_senha"],
        		logado=u["usuario_logado"],
        		admin=u["usuario_admin"])
        	usuarios.append(usuario)
        return usuarios

    def edita_usuario(self, usuario):
        self.execute_query("update usuario set usuario_login = '{}', usuario_senha = '{}' where usuario_id = '{}'".format(usuario.login, usuario.senha, usuario.id), True)

    def deleta_usuario(self, usuario_id):
        self.execute_query("delete from usuario where usuario_id = '{}'".format(usuario_id), True)

     # CRUD - SETOR

    def cadastra_setor(self, setor):
        self.execute_query("insert into setor (setor_nome, setor_situacao, setor_pai) values ('{}', '{}', '{}')".format(setor.nome, setor.situacao, setor.pai), True)

    def get_setores(self):
        data = self.execute_query("select * from setor")
        setores = []
        for d in data:
          setor = Setor(
            id=d["setor_id"],
            nome=d["setor_nome"],
            situacao=d["setor_situacao"])
          setores.append(setor)
        return setores

    def get_setores_ativos(self):
        data = self.execute_query("select * from setor where setor_situacao = 0")
        setores = []
        for d in data:
          setor = Setor(
            id=d["setor_id"],
            nome=d["setor_nome"],
            situacao=d["setor_situacao"])
          setores.append(setor)
        return setores

    def edita_setor(self, setor):
        self.execute_query("update setor set setor_nome = '{}' where setor_id = '{}'".format(setor.nome, setor.id), True)

    def deleta_setor(self, setor_id):
        self.execute_query("update setor set setor_situacao = 1 where setor_id = '{}'".format(setor_id), True)

    # CRUD - FUNCIONARIO

    def cadastra_funcionario(self, funcionario):
        self.execute_query("insert into funcionario (funcionario_nome, funcionario_login, funcionario_senha, setor_id) values ('{}', '{}', '{}', '{}')".format(funcionario.nome, funcionario.login, funcionario.senha, funcionario.setor_id), True)

    def cadastra_funcionario_lotacao(self, funcionario):
        l_id = self.execute_query("insert into funcionario (funcionario_nome, funcionario_login, funcionario_senha, setor_id) values ('{}', '{}', '{}', '{}'); select LAST_INSERT_ID();".format(funcionario.nome, funcionario.login, funcionario.senha, funcionario.setor_id), True)
        self.execute_query("insert into lotacao (funcionario_id, setor_id) values('{}', '{}')".format(funcionario.funcionario_id, l_id), True)

    def get_funcionarios(self):
        data = self.execute_query('''select funcionario_id, funcionario_nome, funcionario_situacao from funcionario''')
        funcionarios = []
        for d in data:
            funcionario = Funcionario(
                          id=d["funcionario_id"],
                          nome=d["funcionario_nome"],
                          situacao=d["funcionario_situacao"])
            funcionarios.append(funcionario)
        return funcionarios

    def edita_funcionario(self, funcionario):
        self.execute_query("update funcionario set funcionario_nome = '{}', funcionario_login = '{}', funcionario_senha = '{}', setor_id = '{}' where funcionario_id = '{}'".format(funcionario.nome, funcionario.login, funcionario.senha, funcionario.setor_id, funcionario.id), True)

    def deleta_funcionario(self, funcionario_id):
        self.execute_query("update funcionario set funcionario_situacao = 1 where funcionario_id = '{}'".format(funcionario_id), True)

    def get_funcionario(self, id):
        data = self.execute_query('''select funcionario_id, funcionario_nome, funcionario_situacao from funcionario where funcionario_id = {}'''.format(id))
        if len(data) < 1:
        	return None
        funcionarios = []
        for d in data:
        	funcionario = Funcionario(
                              id=d["funcionario_id"],
                              nome=d["funcionario_nome"],
                              situacao=d["funcionario_situacao"])
        	funcionarios.append(funcionario)
        return funcionarios[0]

    def get_setor(self, id):
        data = self.execute_query("select * from setor where setor_id = {}".format(id))
        if len(data) < 1:
        	return None
        setores = []
        for d in data:
            setor = Setor(
                    id=d["setor_id"],
                    nome=d["setor_nome"],
                    situacao=d["setor_situacao"])
            setores.append(setor)
        return setores[0]

    # CRUD - USUARIO

    def get_usuarios(self):
        data = self.execute_query('''select * from usuario''')
        usuarios = []
        for d in data:
            usuario = Usuario(
                          id=d["usuario_id"],
                          login=d["usuario_login"],
                          senha=d["usuario_senha"],
                          logado=d["usuario_logado"],
                          admin=d["usuario_admin"])
            usuarios.append(usuario)
        return usuarios


    def get_usuario(self, id):
        data = self.execute_query('''select * from usuario where usuario_id = {}'''.format(id))
        if len(data) < 1:
            return None
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=d["usuario_id"],
                login=d["usuario_login"],
                senha=d["usuario_senha"],
                logado=d["usuario_logado"],
                admin=d["usuario_admin"])
            usuarios.append(usuario)
        return usuarios[0]
