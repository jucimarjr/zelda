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

    def get_funcionalidades(self):
        data = self.execute_query("select * from funcionalidade")
        if len(data) < 1:
            return None
        funcionalidades = []
        for d in data:
            funcionalidade = Funcionalidade(
                              funcionalidade_id=d["funcionalidade_id"],
                              funcionalidade_codigo=d["funcionalidade_codigo"],
                              funcionalidade_nome=d["funcionalidade_nome"],
                              funcionalidade_desc=d["funcionalidade_desc"],
                              funcionalidade_caminho=d["funcionalidade_caminho"],
                              funcionalidade_caminho_imagem=d["funcionalidade_caminho_imagem"],
                              funcionalidade_status=d["funcionalidade_status"],
                              sistema_id=d["sistema_id"])
            funcionalidades.append(funcionalidade)
        return funcionalidades