from flask_mysqldb import MySQL
from .funcionario_modelo import Funcionario
from ..lotacao.lotacao_modelo import Lotacao

class FuncionarioInterface:

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

    # CRUD - FUNCIONARIO

    def cadastra_funcionario(self, funcionario):
        self.execute_query("insert into funcionario (funcionario_nome) values ('{}')".format(funcionario.nome), True)
        data = self.execute_query("select funcionario_id from funcionario order by funcionario_id desc limit 1")

        if len(data) < 1:
            return None

        return data[0]["funcionario_id"]

    def cadastra_lotacao(self, lotacao):
        self.execute_query("insert into lotacao (funcionario_id, setor_id)  values('{}', '{}')" .format(lotacao.funcionario_id, lotacao.setor_id), True)

    def get_lotacao_ativa(self, funcionario_id):
        data = self.execute_query("select * from lotacao where lotacao.funcionario_id = '{}' order by lotacao.lotacao_id desc limit 1".format(funcionario_id))

        if len(data) < 1:
            return None

        for d in data:
            lotacao = Lotacao(
                    id=d["lotacao_id"],
                    funcionario_id=d["funcionario_id"],
                    setor_id=d["setor_id"])

        return lotacao

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
        self.execute_query("update funcionario set funcionario_nome = '{}', funcionario_situacao ='{}' where funcionario_id = '{}'".format(funcionario.nome, funcionario.situacao, funcionario.id), True)

    def deleta_funcionario(self, funcionario_id):
        self.execute_query("update funcionario set funcionario_situacao = 1 where funcionario_id = '{}'".format(funcionario_id), True)

    def get_funcionario(self, id):
        data = self.execute_query('''select funcionario_id, funcionario_nome, funcionario_situacao from funcionario where  funcionario_id = {}'''.format(id))
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
