from flask_mysqldb import MySQL
class SetorInterface:

    def __init__(self, app):
        self.mysql = MySQL(app)

    def execute_query(self, query, insert=False):
        cur = self.mysql.connection.cursor()
        cur.execute(query)

        if insert:
            self.mysql.connection.commit()
        
        data = cur.fetchall()
        cur.close()

        return data
        
    # CRUD - SETOR

    def cadastra_setor(self, setor):
        setor_pai = 'NULL'
        if setor.get_pai() is not None:
            setor_pai = setor.get_pai()
        
        self.execute_query("insert into setor (setor_nome, setor_pai) values (\"{}\", {})".format(setor.nome,setor_pai), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from setor")
        return data[0]['last']


    def get_setores_ids(self):
        data = self.execute_query("select setor_id from setor")
        ids = []

        if data is not None:
            for d in data:
                ids.append(d['setor_id'])

        return ids

    def get_setores_ativos_ids(self):
        data = self.execute_query("select setor_id from setor where setor_situacao = 0")
        ids = []

        if data is not None:
            for d in data:
                ids.append(d['setor_id'])

        return ids

    def edita_setor(self, setor):
        setor_pai = 'NULL'
        if setor.get_pai() is not None:
            setor_pai = setor.get_pai()

        self.execute_query("update setor set setor_nome = '{}', setor_pai = {} where setor_id = '{}'".format(setor.nome, setor_pai, setor.get_id()), True)

    def desativa_setor(self, setor_id):
        self.execute_query("update setor set setor_situacao = 1  where setor_id = '{}'".format(setor_id), True)

    def get_setor(self, setor_id):
        data = self.execute_query("select * from setor where setor_id = {} limit 1".format(setor_id))

        if len(data) < 1:
            return None

        return data[0]