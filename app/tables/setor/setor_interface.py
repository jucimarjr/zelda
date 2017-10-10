from flask_mysqldb import MySQL
from .setor_modelo import Setor


class SetorInterface:

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
        
    # CRUD - SETOR

    def cadastra_setor(self, setor):
        self.execute_query("insert into setor (setor_nome) values (\"{}\")".format(setor.nome), True)

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
        self.execute_query("update setor set setor_situacao = 1  where setor_id = '{}'".format(setor_id), True)

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
