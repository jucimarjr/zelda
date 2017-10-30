from flask_mysqldb import MySQL

class FuncionalidadeInterface:
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

    def get_funcionalidade(self, funcionalidade_id):
        data = self.execute_query("select * from funcionalidade where funcionalidade_id = '{}' limit 1".format(funcionalidade_id))
        return data[0]
        
    def cadastra_funcionalidade(self, funcionalidade):
        self.execute_query("insert into funcionalidade(funcionalidade_nome, funcionalidade_codigo, funcionalidade_desc, sistema_id) values('{}', '{}', '{}', '{}')".format(funcionalidade.nome, funcionalidade.codigo, funcionalidade.desc, funcionalidade.get_sistema().get_id()), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from funcionalidade")

        if len(data) < 1:
            return None

        return data[0]["last"]

    def get_funcionalidades_usuario(self,user_id):
        data = self.execute_query("select F.* from funcionalidade as F, permissao as P, usuario as U where P.perfil_id = U.perfil_id AND P.funcionalidade_id = F.funcionalidade_id AND U.usuario_id = '{}'".format(user_id))
        return data

    def get_funcionalidades(self):
        data = self.execute_query('''select * from funcionalidade''')
        return data

    def edita_funcionalidade(self, funcionalidade):
        self.execute_query("update funcionalidade set funcionalidade_nome = '{}', funcionalidade_codigo = '{}', funcionalidade_desc = '{}' where funcionalidade_id = '{}'".format(funcionalidade.nome, funcionalidade.codigo, funcionalidade.desc, funcionalidade.get_id()), True)

    def desativa_funcionalidade(self, funcionalidade_id):
        self.execute_query("update funcionalidade set funcionalidade_status = 1 where funcionalidade_id = '{}'".format(funcionalidade_id), True)