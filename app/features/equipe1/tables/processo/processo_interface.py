from .....cursor import db

class ProcessoInterface:
    @staticmethod
    def cadastra_processo(processo):
        db.execute_query("INSERT INTO processo (descricao, tipo, usuario_id) VALUES ('{}', '{}', '{}')".format(processo.descricao, processo.tipo, processo.get_usuario().get_id()), True)
        data = db.execute_query("SELECT LAST_INSERT_ID() as last FROM processo")
        return data[0]['last']

    @staticmethod
    def edita_processo(processo):
        db.execute_query("UPDATE processo SET descricao = '{}', tipo = '{}' WHERE processo_id = '{}'".format(processo.descricao, processo.tipo, processo.get_id()), True)

    @staticmethod
    def edita_processo_usuario(processo):
        db.execute_query("UPDATE processo SET usuario_id = '{}' WHERE processo_id = '{}'".format(processo.get_usuario().get_id(), processo.get_id()), True)

    @staticmethod
    def get_processo(id_processo):
        return db.execute_query("SELECT * FROM processo WHERE processo_id = '{}' LIMIT 1".format(id_processo))

    @staticmethod
    def deleta_processo(id_processo):
        db.execute_query("DELETE FROM processo WHERE processo_id = '{}'".format(id_processo), True)

    @staticmethod
    def get_processos_ids():
        return db.execute_query("SELECT processo_id FROM processo")
