from flask_mysqldb import MySQL

class ProcessoInterface():

	def __init__(self, app):
		self.mysql = MySQL(app)

	def execute_query(self, query, insert = False):
		cur = self.mysql.connection.cursor()
		cur.execute(query)
		if insert:
			self.mysql.connection.commit()
		else:
			data = cur.fetchall()
			cur.close()
			if len(data) < 1:
				return None
			return data

	def get_processo(self, processo_id):
		data = self.execute_query("select * from processo where processo_id = '{}' limit 1".format(processo_id))
		return data[0]

	def get_processo_ids(self):
		data = self.execute_query("select * from processo")
		return data

	def cadastra_processo(self, processo):
		self.execute_query("insert into processo(processo_id, processo_tipo, processo_status)\
		 values ('{}', '{}', '{}')".format(processo.id, processo.tipo, processo.get_status()), True)
		data = self.execute_query("select LAST_INSERT_ID() as last from processo")
		return data[0]['last']

	def edita_processo(self, processo):
		self.execute_query("update processo set processo_id = '{}', processo_tipo = '{}' where processo_id = '{}'".format(processo.id, processo.tipo, processo.get_id()), True)

	def desativa_processo(self, processo_id):
		self.execute_query("update processo set processo_status = 1 where processo_id = '{}'".format(processo_id), True)

	def ativa_processo(self, processo_id):
		self.execute_query("update processo set processo_status = 0 where processo_id = '{}'".format(processo_id), True)