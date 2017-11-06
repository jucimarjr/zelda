from flask_mysqldb import MySQL

class SistemaInterface():

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

	def get_sistema(self, sistema_id):
		data = self.execute_query("select * from sistema where sistema_id = '{}' limit 1".format(sistema_id))
		return data[0]

	def get_sistemas_ids(self):
		data = self.execute_query("select * from sistema")
		return data

	def cadastra_sistema(self, sistema):
		self.execute_query("insert into sistema(sistema_nome, sistema_desc, sistema_status, sistema_prefixo)\
		 values ('{}', '{}', '{}', '{}')".format(sistema.nome, sistema.desc, sistema.get_status(), sistema.prefixo), True)
		data = self.execute_query("select LAST_INSERT_ID() as last from sistema")
		return data[0]['last']

	def edita_sistema(self, sistema):
		self.execute_query("update sistema set sistema_nome = '{}', sistema_desc = '{}', sistema_prefixo = '{}' where sistema_id = '{}'".format(sistema.nome, sistema.desc, sistema.prefixo, sistema.get_id()), True)

	def desativa_sistema(self, sistema_id):
		self.execute_query("update sistema set sistema_status = 1 where sistema_id = '{}'".format(sistema_id), True)

	def ativa_sistema(self, sistema_id):
		self.execute_query("update sistema set sistema_status = 0 where sistema_id = '{}'".format(sistema_id), True)