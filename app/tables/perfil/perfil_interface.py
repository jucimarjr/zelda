from flask_mysqldb import MySQL

class PerfilInterface:

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

    # CRUD - PERFIL

    def cadastra_perfil(self, perfil):
        self.execute_query("insert into perfil (perfil_nome) values ('{}')".format(perfil.nome), True)
        data = self.execute_query("select perfil_id from perfil order by perfil_id desc limit 1")

        return data[0]["perfil_id"]

    def edita_perfil(self, perfil):
        self.execute_query("update perfil set perfil_nome = '{}' where perfil_id = '{}'".format(perfil.nome, perfil.get_id()), True)

    def deleta_perfil(self, perfil_id):
        self.execute_query("delete from permissao where perfil_id = '{}'".format(perfil_id), True)
        self.execute_query("delete from perfil where perfil_id = '{}'".format(perfil_id), True)

    def cadastra_permissao(self, permissao):
        self.execute_query("insert into permissao (funcionalidade_id, perfil_id)  values('{}', '{}')" .format(permissao.get_funcionalidade().get_id(), permissao.get_perfil_id()), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from permissao")
        return data[0]

    def remove_permissao(self, permissao_id):
        self.execute_query("delete from permissao where permissao_id = '{}'".format(permissao_id), True)

    def get_perfil(self, perfil_id):
        data = self.execute_query("select * from perfil where perfil_id = '{}'".format(perfil_id))
        return data

    def get_perfis_ids(self):
        data = self.execute_query("select perfil_id from perfil")
        return data

    def get_permissoes_ids(self, perfil_id):
        data = self.execute_query("select permissao_id from permissao where perfil_id = '{}'".format(perfil_id))
        return data

    def get_permissao(self, permissao_id):
        data = self.execute_query("select * from permissao where permissao_id = '{}' limit 1".format(permissao_id))
        return data