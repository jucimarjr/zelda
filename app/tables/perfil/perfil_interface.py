from flask_mysqldb import MySQL
from .perfil_modelo import Perfil

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

    def cadastra_perfil(self, perfil, funcionalidade_id):
        self.execute_query("insert into perfil (perfil_nome) values ('{}')".format(perfil_nome), True)
        data = self.execute_query("select perfil_nome from perfil order by perfil_nome desc limit 1")

        if len(funcionalidade_id) > 1:
            for id in funcionalidade_id:
                permissao = Permissao()
                permissao.funcionalidade_id = id
                permissao.perfil_id = data[0]['perfil_id']
                self.cadastra_permissao(permissao)

        return data[0]["perfil_id"]

    def edita_perfil(self, perfil, funcionalidade_id):
        self.execute_query("update perfil set perfil_nome = '{}' where perfil_id = '{}'".format(perfil.nome, perfil.id), True)

        if len(funcionalidade_id) > 1:
            self.execute_query("delete permissao where perfil_id = '{}'".format(perfil_id), True)
            for id in funcionalidade_id:
                permissao = Permissao()
                permissao.funcionalidade_id = id
                permissao.perfil_id = data[0]['perfil_id']
                self.cadastra_permissao(permissao)

    def deleta_perfil(self, perfil_id):
        self.execute_query("delete permissao where perfil_id = '{}'".format(perfil_id), True)
        self.execute_query("delete perfil where perfil_id = '{}'".format(perfil_id), True)

    def cadastra_permissao(self, permissao):
        self.execute_query("insert into permissao (funcionalidade_id, perfil_id)  values('{}', '{}')" .format(permissao.funcionalidade_id, permissao.perfil_id), True)

    def retorna_permissao_ativa(self, perfil_id):
        data = self.execute_query("select * from permissao where permissao.funcionalidade_id = '{}' order by permissao.permissao_id desc limit 1".format(funcionalidade_id))

        if len(data) < 1:
            return None

        for d in data:
            permissao = Permissao(
                    id=d["permissao_id"],
                    funcionalidade_id=d["funcionalidade_id"],
                    perfil_id=d["perfil_id"])

        return permissao

    def get_funcionalidades(self):
        data = self.execute_query('''select funcionalidade_id, funcionalidade_nome from funcionalidade''')

        if len(data) < 1:
            return None

        funcionalidade = []

        for d in data:
            funcionalidade.append({'id':d['funcionalidade_id'], 'nome':d['funcionalidade_nome']})

        return funcionalidade
