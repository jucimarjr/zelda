from flask_mysqldb import MySQL
from .funcionario import Funcionario
from .setor import Setor

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
            situacao=d["setor_situacao"],
			pai=d["setor_pai"])
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
	
    def get_funcionarios(self):
        data = self.execute_query('''select funcionario_id, funcionario_nome, funcionario_login, funcionario_situacao, setor.setor_id, setor_nome, setor_situacao from funcionario, setor where funcionario.setor_id = setor.setor_id''')
        funcionarios = []
        for d in data:
            funcionario = Funcionario(
                          id=d["funcionario_id"],
                          nome=d["funcionario_nome"],
                          login=d["funcionario_login"],
                          situacao=d["funcionario_situacao"],
                          setor_id=d["setor_id"],
                          setor_nome=d["setor_nome"],
                          setor_situacao=d["setor_situacao"])
            funcionarios.append(funcionario)
        return funcionarios

    def edita_funcionario(self, funcionario):
        self.execute_query("update funcionario set funcionario_nome = '{}', funcionario_login = '{}', funcionario_senha = '{}', setor_id = '{}' where funcionario_id = '{}'".format(funcionario.nome, funcionario.login, funcionario.senha, funcionario.setor_id, funcionario.id), True)

    def deleta_funcionario(self, funcionario_id):
        self.execute_query("update funcionario set funcionario_situacao = 1 where funcionario_id = '{}'".format(funcionario_id), True)

    def get_funcionario(self, id):
        data = self.execute_query('''select funcionario_id, funcionario_nome, funcionario_login, funcionario_situacao, setor.setor_id, setor_nome, setor_situacao from funcionario, setor where funcionario_id = {} and funcionario.setor_id = setor.setor_id'''.format(id))
        if len(data) < 1:
        	return None
        funcionarios = []
        for d in data:
        	funcionario = Funcionario(
                              id=d["funcionario_id"],
                              nome=d["funcionario_nome"],
                              login=d["funcionario_login"],
                              situacao=d["funcionario_situacao"],
                              setor_id=d["setor_id"],
                              setor_nome=d["setor_nome"],
                              setor_situacao=d["setor_situacao"])
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
                    situacao=d["setor_situacao"],
					pai=d["setor_pai"])
            setores.append(setor)
        return setores[0]