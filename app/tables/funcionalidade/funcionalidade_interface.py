from flask_mysqldb import MySQL
from .funcionalidade_modelo import Funcionalidade

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

    def get_funcionalidades_usuario(self,user_id):
        data = self.execute_query("select F.* from funcionalidade as F, permissao as P, usuario as U where P.perfil_id = U.perfil_id AND P.funcionalidade_id = F.funcionalidade_id AND U.usuario_id = '{}'".format(user_id))
        if len(data) < 1:
            return None
        funcionalidades = []
        for d in data:
            funcionalidade = Funcionalidade(
                              funcionalidade_id=d["F.funcionalidade_id"],
                              funcionalidade_codigo=d["F.funcionalidade_codigo"],
                              funcionalidade_nome=d["F.funcionalidade_nome"],
                              funcionalidade_desc=d["F.funcionalidade_desc"],
                              funcionalidade_caminho=d["F.funcionalidade_caminho"],
                              funcionalidade_caminho_imagem=d["F.funcionalidade_caminho_imagem"],
                              funcionalidade_status=d["F.funcionalidade_status"],
                              sistema_id=d["F.sistema_id"])
            funcionalidades.append(funcionalidade)
        return funcionalidades