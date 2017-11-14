from flask_mysqldb import MySQL

class ProcessoInterface:

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

	def salva_processo(self, processo_nome_aluno, processo_tipo, processo_descricao):
		self.execute_query("insert into processo (processo_nome_aluno, processo_tipo, processo_descricao, processo_link) values('{}', '{}', '{}', '')" .format(processo_nome_aluno, processo_tipo, processo_descricao), True)

	def get_processos(self):
		return self.execute_query("SELECT * FROM `processo` ")

	def edit(self, processo_nome_aluno, processo_tipo, processo_descricao, processo_id):
		self.execute_query("update processo set processo_nome_aluno = '{}', processo_tipo = '{}', processo_descricao = '{}' where processo_id = '{}'".format(processo_nome_aluno, processo_tipo, processo_descricao, processo_id), True)

	def deletar(self, processo_id):
		self.execute_query("DELETE FROM `processo` WHERE processo_id = '{}'".format(processo_id), True)
		