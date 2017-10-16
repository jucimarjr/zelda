from flask_mysqldb import MySQL
from .perfil_modelo import Perfil
from ..permissao.permissao_modelo import Permissao

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

    def edita_perfil(self, perfil, funcionalidade_id):
        self.execute_query("update perfil set perfil_nome = '{}' where perfil_id = '{}'".format(perfil.nome, perfil.id), True)

        if len(funcionalidade_id) > 1:
            self.execute_query("delete permissao where perfil_id = '{}'".format(perfil_id), True)
            for id in funcionalidade_id:
                permissao = Permissao()
                permissao.funcionalidade_codigo = id
                permissao.perfil_id = data[0]['perfil_id']
                self.cadastra_permissao(permissao)

    def deleta_perfil(self, perfil_id):
        self.execute_query("delete permissao where perfil_id = '{}'".format(perfil_id), True)
        self.execute_query("delete perfil where perfil_id = '{}'".format(perfil_id), True)

    def cadastra_permissao(self, permissao):
        self.execute_query("insert into permissao (funcionalidade_codigo, perfil_id)  values('{}', '{}')" .format(permissao.funcionalidade_codigo, permissao.perfil_id), True)

    def retorna_permissao_ativa(self, perfil_id):
        data = self.execute_query("select * from permissao where permissao.perfil_id = '{}' order by permissao.permissao_id desc limit 1".format(perfil_id))
        if len(data) < 1:
            return None
        permissoes = []
        for d in data:
            permissao = Permissao(
                    id=d["permissao_id"],
                    funcionalidade_codigo=d["funcionalidade_codigo"],
                    perfil_id=d["perfil_id"])
            permissoes.append(permissao)
        return permissao

    def get_perfil_pelo_id(self, perfil_id):
        data = self.execute_query("select * from perfil where perfil_id = '{}'".format(perfil_id))
        if len(data) < 1:
            return None
        perfis = []
        for d in data:
            perfil = Perfil(
                id = d["perfil_id"],
                nome = d["perfil_nome"])
            perfis.append(perfil)
        return perfis[0]

    def get_funcionalidades(self):
        data = self.execute_query('''select funcionalidade_id, funcionalidade_nome from funcionalidade''')

        if len(data) < 1:
            return None

        funcionalidade = []

        for d in data:
            funcionalidade.append({'id':d['funcionalidade_id'], 'nome':d['funcionalidade_nome']})

        return funcionalidade
