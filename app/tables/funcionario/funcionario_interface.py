from flask_mysqldb import MySQL

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
        data = self.execute_query("select LAST_INSERT_ID() as last from funcionario")
        return data[0]['last']

    def cadastra_lotacao(self, funcionario_id, lotacao):
        self.execute_query("insert into lotacao (funcionario_id, setor_id)  values('{}', '{}')" .format(funcionario_id, lotacao.get_setor().get_id()), True)

    def get_lotacao_ativa(self, funcionario_id):
        data = self.execute_query("select * from lotacao where lotacao.funcionario_id = '{}' order by lotacao.lotacao_id desc limit 1".format(funcionario_id))

        if len(data) < 1:
            return None

        return data[0]

    def get_funcionarios_ids(self):
        data = self.execute_query("select funcionario_id from funcionario")
        return data

    def edita_funcionario(self, funcionario):
        self.execute_query("update funcionario set funcionario_nome = '{}' where funcionario_id = '{}'".format(funcionario.nome, funcionario.get_id()), True)

    def deleta_funcionario(self, funcionario_id):
        self.execute_query("update funcionario set funcionario_situacao = 1 where funcionario_id = '{}'".format(funcionario_id), True)

    def get_funcionario(self, funcionario_id):
        data = self.execute_query("select * from funcionario where funcionario_id = '{}' limit 1".format(funcionario_id))
        if len(data) < 1:
            return None
        return data[0]
